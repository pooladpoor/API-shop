# Generated by Django 5.1.1 on 2024-09-23 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accuont', '0005_alter_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]