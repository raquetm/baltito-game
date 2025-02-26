# users/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Review 

# tengo que arreglar bien todos los forms

class UserRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100)
    subscribed = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                full_name=self.cleaned_data['full_name'],
                subscribed=self.cleaned_data['subscribed']
            )
        return user

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter review title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your review here...'}),
        }