from django.shortcuts import render
from django.http import JsonResponse
from twilio.rest import Client
from .models import SMS
from django.conf import settings

def send_sms(request):
    context = {} 
    if request.method == 'POST':
        recipient = "+639121769168"
        message = request.POST.get('message')

        # Send SMS using Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        
        try:
            sms = client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=recipient
            )
            # Save to the database
            SMS.objects.create(recipient=recipient, message=message)
            context['message'] = 'SMS sent successfully!'
            context['message_type'] = 'success'
        except Exception as e:
            context['message'] = 'Failed to send SMS.'
            context['message_type'] = 'error'

    return render(request, 'sms/send_sms.html', context)


def home(request):
    return render(request, 'home.html')