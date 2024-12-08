from django.urls import path
from . import views

urlpatterns = [
    path('sms/', views.send_sms, name='send_sms'),
    path('', views.home, name='home'),
]
