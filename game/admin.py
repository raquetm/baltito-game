from django.contrib import admin
from .models import Update, UserScore

# registra el modelo Update en el panel de administración de Django
admin.site.register(Update)
admin.site.register(UserScore)