# Generated by Django 4.2 on 2023-04-17 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_new_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
    ]
