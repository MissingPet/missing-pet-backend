# Generated by Django 3.1.2 on 2020-11-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0005_auto_20201113_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='animal_type',
            field=models.IntegerField(
                choices=[(1, 'Собаки'), (2, 'Кошки'), (3, 'Иное')], verbose_name='Тип животного'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='photo',
            field=models.ImageField(
                upload_to='announcements/%Y/%m/%d/', verbose_name='Фотография животного'),
        ),
    ]
