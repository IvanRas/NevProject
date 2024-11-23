from django.contrib import admin
from .models import Recipient

# Register your models here.


@admin.register(Recipient)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'email', 'comment')
    list_filter = ('last_name',)
    search_fields = ('last_name', 'content',)
