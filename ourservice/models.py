from django.db import models
# from contactform.models import Contactform
# Create your models here.
# class Service (models.Model):
#     service_title=models.CharField(max_length=150)
#     service_desc=models.TextField()
#     service_read_link=models.CharField( max_length=150)

# from django.db import models
# Create your models here.
class Contactform (models.Model):
    fullname=models.CharField( max_length=150)
    email=models.CharField( max_length=150)
    subject=models.CharField( max_length=150)
    message=models.CharField( max_length=250)
