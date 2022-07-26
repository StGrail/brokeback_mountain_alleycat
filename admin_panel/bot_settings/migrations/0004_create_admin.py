# Generated by Django 4.1 on 2022-09-10 13:35
import os
from django.db import migrations


def create_admin(apps, schema_editor) -> None:
    """Создаем суперюзера для доступа в админку и обращения к апи"""

    UserModel = apps.get_model('auth', 'User')

    admin_name = os.environ.get('ADMIN_NAME')
    admin_password = os.environ.get('ADMIN_PASSWORD')

    if admin_name and admin_password:

        if not UserModel.objects.filter(username=admin_name, is_superuser=True).exists():
            admin_user = UserModel.objects.create_superuser(
                username=admin_name, password=admin_password
            )
            admin_user.save()
    else:
        raise AttributeError(
            'Нет переменных ADMIN_NAME и ADMIN_PASSWORD для создания админ пользователя.'
        )


def reverse_func(apps, schema_editor) -> None:
    '''Откат миграции'''
    pass


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("bot_settings", "0003_custommessage"),
    ]

    operations = [migrations.RunPython(create_admin, reverse_func)]
