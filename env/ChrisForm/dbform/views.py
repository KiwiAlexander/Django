from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
import requests
import json
import urllib.request
from django.contrib.auth.decorators import login_required
import datetime
from .models import Job, Volunteer, Client

# Create your views here.

def job(request):
    if request.method == 'POST':
        volunteer = request.POST.get('volunteer')
        client = request.POST.get('client')
        date = request.POST.get('date')
        summary = request.POST.get('summary')
        location = request.POST.get('location')
        temp = Job(Volunteer=volunteer, Client=client, Date=date, Summary=summary, Location=location)
        temp.save()
    return render(request, 'dbform/job.html')

def client(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        notes = request.POST.get('notes')
        temp = Client(First_Name=first, Last_Name=last, Phone=phone, Email=email, Notes=notes)
        temp.save()
    return render(request, 'dbform/client.html')

def volunteer(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        temp = Volunteer(First_Name=first, Last_Name=last, Phone=phone, Email=email)
        temp.save()
    return render(request, 'dbform/volunteer.html')