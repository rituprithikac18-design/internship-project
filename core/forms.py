# contains forms for user registration, client creation, and video upload
# core/forms.py
# This file contains forms for user registration, client creation, and video upload
# It uses Django's built-in forms and custom forms for specific models.
# Ensure to import necessary models and forms from Django.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Client, Video


# ------------------------
# User Registration Forms
# ------------------------

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')  # Extend with more fields if needed


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# ------------------------
# Client Creation Form
# ------------------------

class ClientUserForm(forms.ModelForm):
    # User-related fields
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    # Client-related fields
    company_logo = forms.ImageField(required=False)

    class Meta:
        model = Client
        fields = ['company_name', 'site', 'company_logo']


# ------------------------
# Video Upload (Admin)
# ------------------------

class AdminUploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['client', 'site', 'video']


# ------------------------
# Filter Videos
# ------------------------

class VideoFilterForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=True)
    site_name = forms.CharField(max_length=255, required=True)


# ------------------------
# Video Upload Form
# ------------------------

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['site', 'video']
