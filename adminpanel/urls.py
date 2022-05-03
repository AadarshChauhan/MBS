from django import views
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sms.html', views.sms, name="sms"),
    path('mail.html', views.mail, name="mail"),
    path('whatsapp.html', views.whatsapp, name="whatsapp"),
    path('mms.html', views.mms, name="mms"),
    path('contacts.html', views.contacts, name="contacts"),
    # path('contacts1.html', views.contacts1, name="contacts1")

]
