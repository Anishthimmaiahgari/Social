# Generated by Django 3.0.8 on 2021-02-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='action',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('COLORIZED', 'colorized'), ('GRAYSCALE', 'grayscale'), ('BLURRED', 'blurred'), ('BINARY', 'binary'), ('INVERT', 'invert')], max_length=50, null=True),
        ),
    ]
