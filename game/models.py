from django.db import models
from users.models import UserProfile  # importa el modelo UserProfile desde la aplicación users

# modelo para almacenar las puntuaciones de los usuarios 
class UserScore(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # crea una relación muchos a uno con el modelo UserProfile.
    # si el perfil de usuario se elimina, todas las puntuaciones asociadas también se eliminarán (on_delete=models.CASCADE).
    score = models.IntegerField() 
    played_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.score}"

# modelo para gestionar actualizaciones desde admin
class Update(models.Model):
    title = models.CharField(max_length=200)    
    date = models.DateField()    
    content = models.TextField()    
    image = models.ImageField(upload_to='updates/', blank=True, null=True)

    def __str__(self):
        return self.title
