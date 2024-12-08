##SMS Twilio Django Project
#This project demonstrates how to integrate Twilio with a Django application to send SMS messages. Follow the steps below to set up the project on your local machine.
________________________________________
##Table of Contents
1.	Prerequisites
2.	Python Setup
3.	Django Setup
4.	Install Dependencies
5.	Project Configuration
6.	Creating the SMS App
7.	Run the Application
8.	Testing
________________________________________
##Prerequisites
Before you start, make sure you have the following installed on your machine:
•	Python (>=3.7)
•	pip (Python package installer)
You can download Python from the official website:
Python Official Website
________________________________________
##1. Python Setup
1.1 Install Python
1.	Download and install Python from the official website:
Download Python
2.	Ensure Python is added to the PATH during installation. This allows you to run Python and pip commands from the terminal.
1.2 Install Pipenv
Pipenv is a tool that simplifies package management for Python projects. It automatically creates and manages a virtual environment for your project.
To install Pipenv globally, run the following command:
bash
Copy code
pip install pipenv
1.3 Set Up Virtual Environment
Once Pipenv is installed, you can create a virtual environment for your project:
1.	Navigate to your project folder:
bash
Copy code
cd /path/to/your/project
2.	Install the virtual environment:
bash
Copy code
pipenv install
3.	Activate the virtual environment:
bash
Copy code
pipenv shell
Now your virtual environment is ready.
________________________________________
##2. Django Setup
2.1 Install Django
Install Django using pipenv:
bash
Copy code
pipenv install django
2.2 Create a Django Project
Once Django is installed, create a new Django project using the following command:
bash
Copy code
django-admin startproject sms_twilio
This creates a new folder sms_twilio with the default Django project structure.
2.3 Create a Django App
Now create a Django app where you will implement the logic for sending SMS. Run the following command:
bash
Copy code
python manage.py startapp sms
This will create a folder named sms where you’ll add your views, models, and templates.
________________________________________
##3. Install Dependencies
3.1 Install Twilio
Twilio is a cloud communications platform used to send SMS messages. Install the Twilio library by running:
bash
Copy code
pipenv install twilio
3.2 Install python-dotenv
To keep your credentials secure, you can use python-dotenv to load environment variables from a .env file. Install it with:
bash
Copy code
pipenv install python-dotenv
________________________________________
##4. Project Configuration
4.1 Create a Twilio Account
To use Twilio for sending SMS, you need to create an account on Twilio's website.
Once registered, you'll be provided with the following credentials:
•	Account SID
•	Auth Token
•	Twilio Phone Number
4.2 Configure Environment Variables
Create a .env file at the root of your project directory to store sensitive information like your Twilio credentials. Your .env file should look like this:
plaintext
Copy code
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
4.3 Load Environment Variables in Django Settings
In your sms_twilio/settings.py, load these environment variables securely using python-dotenv.
1.	At the top of settings.py, import dotenv:
python
Copy code
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
2.	Then, replace the sensitive data with values from the environment variables:
python
Copy code
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
________________________________________
##5. Creating the SMS App
5.1 Create the SMS Model
In sms/models.py, create a model to store SMS details (optional). Here’s a simple example:
python
Copy code
# sms/models.py
from django.db import models

class SMS(models.Model):
    to_number = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS to {self.to_number} at {self.sent_at}"
5.2 Apply Migrations
Run the following commands to create the database tables for your model:
bash
Copy code
python manage.py makemigrations sms
python manage.py migrate
________________________________________
##6. Creating the Views and URLs
6.1 Create the SMS Sending Logic
In sms/views.py, add the logic to handle SMS sending using Twilio.
python
Copy code
# sms/views.py
from django.shortcuts import render
from twilio.rest import Client
from django.conf import settings
from .models import SMS

def send_sms(request):
    if request.method == 'POST':
        to_number = request.POST['to_number']
        message = request.POST['message']

        # Send SMS using Twilio
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=to_number
        )

        # Save the SMS to the database (optional)
        SMS.objects.create(to_number=to_number, message=message.body)

        return render(request, 'sms/send_sms.html', {'status': 'Message Sent Successfully!'})

    return render(request, 'sms/send_sms.html')
6.2 Create URLs for the SMS Views
In sms/urls.py, add a URL pattern for the send_sms view:
python
Copy code
# sms/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send_sms, name='send_sms'),
]
In your sms_twilio/urls.py, include the sms app URLs:
python
Copy code
# sms_twilio/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sms/', include('sms.urls')),  # Include the sms app's URLs
]
________________________________________
##7. Run the Application
Once everything is set up, run the development server:
bash
Copy code
python manage.py runserver
Now, you can visit the following URL in your browser to access the app:
perl
Copy code
http://127.0.0.1:8000/sms/send/
________________________________________
##8. Testing
To test the SMS sending functionality:
1.	Ensure that you have your Twilio credentials set correctly in the .env file.
2.	Navigate to the /sms/send/ URL.
3.	Fill in the form with a phone number and message, then submit it.
4.	If successful, you should see a confirmation message that your SMS was sent.
