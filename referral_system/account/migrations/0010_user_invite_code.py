# Generated by Django 4.2.11 on 2024-04-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_user_password_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='invite_code',
            field=models.CharField(default=''),
        ),
    ]
