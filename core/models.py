#contains all the models used for the forms used in the application
# core/models.py
# This file contains the models for user, client, and video.
# It defines the structure of the database tables and their relationships.
# Ensure to import necessary modules from Django.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    company_logo=models.ImageField( upload_to='logos/',blank=True,null=True)
    def __str__(self):
        return f"{self.company_name} - {self.city} - {self.site}"

class Video(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    site = models.CharField(max_length=255)  # this must exist
    video = models.FileField(upload_to='videos/')  # this must exist
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.company_name} - {self.site}"
