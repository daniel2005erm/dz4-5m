# Generated by Django 4.2.1 on 2023-05-21 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='students',
        ),
    ]
