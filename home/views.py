from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from _datetime import datetime 
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about us")    

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is about services")  
def contact(request):   
    if request.method=="POST":
        email=request.POST.get('email') 
        query=request.POST.get('query') 
        contact=Contact(email=email,query=query)
        contact.save()
        messages.success(request, 'Your query has been sent, We will get back to you soon! ')
    return render(request,'contact.html')     

           