from django.contrib import admin
from .models import Update, UserScore

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content')
    search_fields = ('title', 'content')
    list_filter = ('date',)

class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'played_date')
    search_fields = ('user__user__username', 'score')
    list_filter = ('played_date',)
    ordering = ('-score',)

admin.site.register(Update, UpdateAdmin)
admin.site.register(UserScore, UserScoreAdmin)