from django.db import models
from django.contrib.auth.models import User

# Create your models here.h
class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course= models.CharField(max_length=50,null=True,blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    class_grade = models.CharField(max_length=20, null=True, blank=True)
    

    