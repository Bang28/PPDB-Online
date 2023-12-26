from django.contrib import admin
from . models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'level']
    list_filter = ['level']
    search_fields = ['username', 'first_name', 'email']
