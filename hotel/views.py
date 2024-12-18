from django.http import HttpResponse
from django.shortcuts import render


from ourservice.models import Contactform

def ContactPage(request):

    msg=""
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        alldata=Contactform(name=name,email=email,subject=subject,message=message)
        alldata.save() 
        msg="Data Inserted"

    return render(request,"contact.html",{'msg':msg})


# Other views
def HomePage(request):
    return render(request, "index.html")

def aboutUs(request):
    return render(request, "about.html")

def amenitiesPage(request):
    return render(request, "amenities.html")

def bookingPage(request):
    return render(request, "booking.html")

def contactPage(request):
    return render(request, "contact.html")

def loginPage(request):
    return render(request, "login.html")

def roomPage(request):
    return render(request, "room.html")
