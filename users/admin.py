from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('middle_name',)}),
    )
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'middle_name')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'middle_name')

