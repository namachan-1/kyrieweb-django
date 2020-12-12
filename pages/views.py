from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import LeaderProfile, DoulosProfile, MenStudy, WomenStudy, Event

def index(request, *args, **kwargs):
    return render(request, 'home.html', {})


def church(request, *args, **kwargs):
    return render(request, 'church.html', {})


def ministry(request, *args, **kwargs):
    return render(request, 'ministry.html', {})

def event(request, *args, **kwargs):
    return render(request, 'event.html', {})


def leader(request, *args, **kwargs):
    leader = LeaderProfile.objects.all()
    return render(request, 'leader.html', {'leader': leader})


def contact(request, *args, **kwargs):
    if request.method == "POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        status = request.POST['status']
        message = request.POST['message']

        # send an email
        send_mail(
            first_name + ' ' + last_name + ' ' + '(' + status + ')', # subject
            message, # message
            email, # from email
            ['nathaniel.chang828@gmail.com'], # to email
        )

        return render(request, 'contact.html', {'first_name': first_name})

    else:
        return render(request, 'contact.html', {})


def staff(request, *args, **kwargs):
    return render(request, 'staff.html', {})


def doulos(request, *args, **kwargs):
    return render(request, 'doulos.html', {})




