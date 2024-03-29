from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'var':"SENT"
    }
    return render(request,"index.html",context)
    # return HttpResponse("This is homepage")

def services(request):
    # return HttpResponse("This is Services page")
    return render(request,"services.html")

def contact(request):
    # return HttpResponse("This is contact page")
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been received.')
    return render(request,"contact.html")

def about(request):
    # return HttpResponse("This is about us page")
    return render(request,"about.html")