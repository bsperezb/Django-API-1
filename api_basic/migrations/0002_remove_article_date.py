# Generated by Django 3.2.5 on 2021-07-10 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
