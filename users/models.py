from django.db import models
from django.contrib.auth.models import User  # importa el modelo de usuario predeterminado de Django

# modelo para el perfil de usuario
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    # crea una relación uno a uno con el modelo User. 
    # si el usuario se elimina, el perfil de usuario también se eliminará (on_delete=models.CASCADE).
    subscribed = models.BooleanField(default=False)  

    def __str__(self):
        return self.user.username  

# modelo para las reseñas
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    # crea una relación muchos a uno con el modelo User. 
    # si el usuario se elimina, todas las reseñas asociadas también se eliminarán (on_delete=models.CASCADE).
    title = models.CharField(max_length=200)      
    content = models.TextField()      
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title  