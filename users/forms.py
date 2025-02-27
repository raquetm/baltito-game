from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Review

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    subscribed = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'subscribed']
        help_texts = {
            'username': None, 
        }
        labels = {
            'email': 'Email', 
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                subscribed=self.cleaned_data['subscribed']
            )
        return user

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'image']