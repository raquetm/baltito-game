from django.db import models
from users.models import UserProfile

class UserScore(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    score = models.IntegerField()
    played_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.score}"

class Update(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='updates/', blank=True, null=True)

    def __str__(self):
        return self.title