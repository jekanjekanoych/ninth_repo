import os

from twilio.rest import Client
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .tasks import send
from .forms import NumberForm
from .models import Number
from .forms import CodeForm
from .models import Code

account_sid = "AC7672eeb30a47e58c608364845b0deafc"
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
verify_sid = "VA5cdae07c53dba8eaa790b8d842b194d2"
verified_number = "+380639788386"
client = Client(account_sid, auth_token)


def index(request):
    return HttpResponse("Main page")


def send_sms(request):
    if request.method == "GET":
        form = NumberForm()
        context = {"form": form}
        return render(request, "send_sms.html", context)
    else:
        request.method == "POST"
    form = NumberForm(request.POST)
    if not form.is_valid():
        return HttpResponse(reverse("send_sms"))
    form.save()
    number = request.POST.get("number")
    send(number)
    return HttpResponseRedirect(reverse("send_sms"))


def verification(request):
    if request.method == "GET":
        form = CodeForm()
        context = {"form": form}
        return render(request, "verification.html", context)
    else:
        request.method == "POST"
    form = CodeForm(request.POST)
    if not form.is_valid():
        return HttpResponse(reverse("verification"))
    form.save()
    verification_check = client.verify.v2.services(
        verify_sid
    ).verification_checks.create(
        to=request.POST.get("number"), code=request.POST.get("code")
    )
    return HttpResponse(verification_check.status)
