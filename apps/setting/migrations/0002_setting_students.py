# Generated by Django 4.2.1 on 2023-05-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='students',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество студентов'),
        ),
    ]
