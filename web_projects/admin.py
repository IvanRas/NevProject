from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'email', 'comment')
    list_filter = ('last_name',)
    search_fields = ('last_name', 'content',)
