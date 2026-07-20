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

class Signal(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    site = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('maintenance', 'Maintenance')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.site} ({self.client.company_name})"

class Alert(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    signal = models.ForeignKey(Signal, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alert for {self.client.company_name} - Resolved: {self.resolved}"
