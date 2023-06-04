import os

from celery import shared_task
from twilio.rest import Client

account_sid = "AC7672eeb30a47e58c608364845b0deafc"
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
verify_sid = "VA5cdae07c53dba8eaa790b8d842b194d2"
client = Client(account_sid, auth_token)


@shared_task
def send(number):
    verification = client.verify.v2.services(verify_sid).verifications.create(
        to=number, channel="sms"
    )
