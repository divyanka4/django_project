from django.http import HttpResponse
from django.shortcuts import render


from ourservice.models import Contactform

def contactus(request):
    msg=""
    if request.method =='POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        if not fullname or not email or not subject or not message:
            msg = "All fields are required. Please fill them out."
        else:
            # Save data to the database
            alldata = Contactform(fullname=fullname, email=email, subject=subject, message=message)
            alldata.save()
            msg = "Your message has been successfully sent."
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
