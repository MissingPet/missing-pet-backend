# Generated by Django 3.1.3 on 2021-01-05 14:47
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("announcements", "0012_auto_20210102_2218"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="animal_type",
            field=models.IntegerField(
                choices=[(1, "Собаки"), (2, "Кошки"), (3, "Иные")],
                verbose_name="Тип животного",
            ),
        ),
        migrations.AlterField(
            model_name="announcement",
            name="updated_at",
            field=models.DateTimeField(auto_now=True,
                                       verbose_name="Обновлено"),
        ),
    ]
