# Generated by Django 4.0.6 on 2022-07-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('category', models.IntegerField(choices=[(0, 'Не выбрано'), (1, 'Фикс брейклесс'), (2, 'Мультик, сингл, фикс с тормозами, мтб'), (3, 'Девочки')], default=0, verbose_name='Категория')),
                ('instagram', models.CharField(blank=True, help_text='запрещенная организация на территории Российской Федерации', max_length=64, verbose_name='Инстаграм')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
    ]