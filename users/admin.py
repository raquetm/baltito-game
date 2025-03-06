from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created_at')
    search_fields = ('user__username', 'title', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Review, ReviewAdmin)