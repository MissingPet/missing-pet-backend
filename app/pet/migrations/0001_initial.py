# Generated by Django 3.1.2 on 2021-05-09 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pet.models.objects


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Адрес электронной почты')),
                ('nickname', models.CharField(max_length=64, verbose_name='Никнейм')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус персонала')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Статус суперпользователя')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активирован')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('settings_name', models.CharField(max_length=200, unique=True, verbose_name='Уникальное название настроек')),
                ('actual_app_version_ios', models.CharField(blank=True, max_length=200, null=True, verbose_name='Актуальная версия приложения для ios')),
                ('min_app_version_ios', models.CharField(blank=True, max_length=200, null=True, verbose_name='Минимальная версия приложения для ios')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='PasswordResetConfirmationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(default=pet.models.objects.generate_password_reset_confirmation_code, verbose_name='Код подтвержения')),
                ('expired_in', models.BigIntegerField(default=pet.models.objects.get_expired_in_time, verbose_name='Время устаревания кода')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_reset_codes', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, которому принадлежит этот код')),
            ],
            options={
                'verbose_name': 'Код подтверждения сброса пароля',
                'verbose_name_plural': 'Коды подтверждения сброса пароля',
            },
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=5000, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to=pet.models.objects.upload_photo, verbose_name='Фотография животного')),
                ('announcement_type', models.IntegerField(choices=[(1, 'Потеряно'), (2, 'Найдено')], verbose_name='Тип объявления')),
                ('animal_type', models.IntegerField(choices=[(1, 'Собаки'), (2, 'Кошки'), (3, 'Иные')], verbose_name='Тип животного')),
                ('address', models.CharField(max_length=1000, verbose_name='Место пропажи или находки')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('contact_phone_number', models.CharField(max_length=12, verbose_name='Контактный телефон')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ('-created_at',),
            },
        ),
    ]