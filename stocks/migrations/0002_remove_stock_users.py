# Generated by Django 5.0.7 on 2024-07-12 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='users',
        ),
    ]
