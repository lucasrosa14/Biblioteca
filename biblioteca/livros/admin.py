# admin.py
from django.contrib import admin
from .models import Book, Profile, UserProfile

admin.site.register(Book)
admin.site.register(Profile)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sexo', 'data_nascimento')
    list_filter = ('sexo',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
