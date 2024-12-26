# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        db_table = "alembic_version"
        managed = False


class User(models.Model):
    """
    Модель пользователя.
    """

    tg_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"
        managed = False

    def __str__(self):
        return self.username or f"User {self.tg_id}"


class Wisdom(models.Model):
    """
    Модель мудрости.
    """

    user = models.ForeignKey(User, related_name="wisdoms", on_delete=models.CASCADE)
    wisdom_text = models.CharField(max_length=128, null=True, blank=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "wisdoms"
        managed = False

    def __str__(self):
        return f"{self.author or 'Unknown'}: {self.wisdom_text}"
