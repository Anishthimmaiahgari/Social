# Generated by Django 3.0.8 on 2021-03-02 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20210302_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_online',
        ),
    ]
