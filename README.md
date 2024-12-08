# SMS Twilio Django Project

This project demonstrates how to integrate Twilio with a Django application to send SMS messages. Follow the steps below to set up and run the project on your local machine.

## Table of Contents
- [Prerequisites](#prerequisites)
- [How to Install the Project](#how-to-install-the-project)
  - [Python Setup](#python-setup)
  - [Django Setup](#django-setup)
  - [Install Dependencies](#install-dependencies)
  - [Project Configuration](#project-configuration)
  - [Creating the SMS App](#creating-the-sms-app)
- [Run the Application](#run-the-application)
- [Testing](#testing)

## Prerequisites
Before you start, make sure you have the following installed on your machine:
- **Python (>=3.7)**
- **Git**
- **pip** (Python package installer)

You can download Python from the official website: [Python Official Website](https://www.python.org/).

## How to Install the Project

### 1. Clone the Repository
First, clone this repository from GitHub to your local machine using the following command:
```bash
git clone https://github.com/your-username/sms-twilio-django.git
Replace your-username with your GitHub username.
```

### 2. Navigate to the Project Directory
Move into the project directory:

```bash

cd sms-twilio-django
```
### 3. Set Up the Virtual Environment
Create and activate a virtual environment using pipenv (or any other virtual environment tool of your choice). Install the virtual environment dependencies:

```bash

pipenv install
### Activate the virtual environment:
```bash

pipenv shell
```
## Python Setup
If you haven’t already set up Python and Pipenv, refer to the steps below.

### Install Python
Download and install Python from the official website: Download Python.
Ensure Python is added to the PATH during installation to use Python and pip commands from the terminal.

### Install Pipenv
To install Pipenv globally, run the following command:

```bash

pip install pipenv
```
## Django Setup
### Install Django
Install Django using pipenv:

```bash

pipenv install django
```
### Migrate the Database
Run the following commands to set up the database for the project:

```bash

python manage.py makemigrations
python manage.py migrate
```
## Install Dependencies
Ensure the required dependencies are installed. Run the following commands inside the virtual environment:

### Install Twilio to send SMS messages:

```bash

pipenv install twilio
```
### Install python-dotenv to securely load environment variables:

```bash

pipenv install python-dotenv
```
## Project Configuration
### Add Twilio Credentials
Create a .env file in the project root directory.
Add your Twilio credentials (get them from your Twilio account):
plaintext
```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
```
### Configure Django Settings
In sms_twilio/settings.py, load these credentials:

```python

from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
```
## Creating the SMS App
## Create the SMS Model
#### Define the model for the SMS app in sms/models.py:
```python

from django.db import models

class SMS(models.Model):
    to_number = models.CharField(max_length=15)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SMS to {self.to_number} at {self.sent_at}"
```
## Run migrations to update the database schema:

```bash

python manage.py makemigrations sms
python manage.py migrate
```
## Create Views and URLs
Define the logic for sending SMS in sms/views.py. Then set up the URLs in sms/urls.py and include them in sms_twilio/urls.py.

Refer to the Creating the SMS App section in the main documentation for detailed code.

## Run the Application
### Start the development server:

```bash

python manage.py runserver
Access the application in your browser at:
http://127.0.0.1:8000/sms/send/
```
## Testing
### To test the application:

Navigate to the /sms/send/ page.
Enter a valid phone number and message in the form.
Click the "Send" button. You should see a success message if the SMS is sent successfully.
csharp

