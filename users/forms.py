from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Review

# form para el registro de usuario
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())  #se usa un widget de entrada de contraseña
    subscribed = forms.BooleanField(required=False, label='Subscribe to our newsletter')  

    class Meta:
        model = User  
        fields = ['username', 'email', 'password', 'subscribed']  
        help_texts = {
            'username': None,  # se elimina el texto de ayuda
        }
        labels = {
            'email': 'Email',  
        }

    # método para guardar el formulario
    def save(self, commit=True):
        user = super().save(commit=False)  # guarda el objeto
        user.set_password(self.cleaned_data['password'])  # establece la contraseña

        if commit:  
            user.save()  # guarda el usuario en la base de datos
            UserProfile.objects.create(  
                user=user,  # crea un perfil de usuario asociado al usuario
                subscribed=self.cleaned_data['subscribed']  
            )
        return user  # devuelve el objeto

# form para la reseña
class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review  
        fields = ['title', 'content', 'image']  
