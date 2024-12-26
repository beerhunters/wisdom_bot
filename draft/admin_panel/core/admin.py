from django.contrib import admin
from .models import User, Wisdom


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("tg_id", "username", "full_name", "created_at")
    search_fields = ("tg_id", "username", "full_name")
    list_filter = ("created_at",)


@admin.register(Wisdom)
class WisdomAdmin(admin.ModelAdmin):
    list_display = ("user", "author", "wisdom_text", "created_at")
    search_fields = ("author", "wisdom_text")
    list_filter = ("created_at", "author")
