from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'subscribed']