from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


def home(request):
    return render(request,'ht.html')

def about(request):
    return render(request,'about.html')

def contactus(request):
    if(request.method=='POST'):

        name=request.POST.get('name')
        surname=request.POST.get('surname')
        email=request.POST.get('email')
        need=request.POST.get('need')
        message=request.POST.get('message')
        contact=Contact(name=name,surname=surname,email=email,need=need,message=message,date=datetime.today())
        contact.save()
    
    return render(request,'contactus.html')


