# Generated by Django 3.1.2 on 2021-06-08 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210608_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
