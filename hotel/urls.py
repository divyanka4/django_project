from django.contrib import admin
from django.urls import path
from hotel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage),
    path('about.html', views.aboutUs),
    path('amenities.html', views.amenitiesPage),
    path('booking.html', views.bookingPage),
    path('contact.html', views.contactPage),
    path('login.html', views.loginPage),
    path('room.html', views.roomPage),
       

]