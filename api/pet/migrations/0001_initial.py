# Generated by Django 3.1.2 on 2021-02-04 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254,
                                            unique=True, verbose_name='Адрес электронной почты')),
                ('nickname', models.CharField(max_length=64, verbose_name='Никнейм')),
                ('is_staff', models.BooleanField(
                    default=False, verbose_name='Статус персонала')),
                ('is_superuser', models.BooleanField(
                    default=False, verbose_name='Статус суперпользователя')),
                ('is_active', models.BooleanField(
                    default=True, verbose_name='Активирован')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Обновлён')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(
                    max_length=5000, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='pet/%Y/%m/%d/',
                                            verbose_name='Фотография животного')),
                ('announcement_type', models.IntegerField(choices=[
                 (1, 'Потеряно'), (2, 'Найдено')], verbose_name='Тип объявления')),
                ('animal_type', models.IntegerField(choices=[
                 (1, 'Собаки'), (2, 'Кошки'), (3, 'Иные')], verbose_name='Тип животного')),
                ('address', models.CharField(max_length=1000,
                                             verbose_name='Место пропажи или находки')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('contact_phone_number', models.CharField(
                    max_length=12, verbose_name='Контактный телефон')),
                ('created_at', models.DateTimeField(
                    auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(
                    auto_now=True, verbose_name='Обновлено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='announcements', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
