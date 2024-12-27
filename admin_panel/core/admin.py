from django.contrib import admin

from .models import Users, Wisdoms


# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "tg_id",
        "username",
        "full_name",
        "created_at",
    )  # Поля для отображения
    search_fields = ("tg_id", "username", "full_name")  # Поля для поиска
    list_filter = ("created_at",)  # Фильтр по дате


@admin.register(Wisdoms)
class WisdomsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "wisdom_text",
        "author",
        "created_at",
    )  # Поля для отображения
    search_fields = ("wisdom_text", "author", "user__tg_id")  # Поля для поиска
    list_filter = ("created_at",)  # Фильтр по дате
