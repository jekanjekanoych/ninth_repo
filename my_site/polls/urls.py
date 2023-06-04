from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("send_sms/", views.send_sms, name="send_sms"),
    path("verification/", views.verification, name="verification"),
]
