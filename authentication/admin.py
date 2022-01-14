from django.contrib import admin
from .models import CustomUser

# Sets Auth to use Custom User Model
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
