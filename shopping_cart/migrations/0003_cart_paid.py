# Generated by Django 5.1.1 on 2024-09-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]