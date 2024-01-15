from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ['profile', 'username', 'email']
    list_filter = ['is_superuser']
    search_fields = ['username', 'first_name', 'email']
    list_per_page = (5)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
