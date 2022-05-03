from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def sms(request):
    return render(request, 'sms.html', {})


def mail(request):
    return render(request, 'mail.html', {})


def whatsapp(request):
    return render(request, 'whatsapp.html', {})


def mms(request):
    return render(request, 'mms.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


# def contacts1(request):
#     return render(request, 'contacts1.html', {})

# Create your views here.
