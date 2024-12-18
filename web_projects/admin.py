from django.contrib import admin
from web_projects.models import User, Message, NewsLetter, Mailing

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("last_name", "id", "email", "comment",)
    search_fields = ("last_name", "comment")
