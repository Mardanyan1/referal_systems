# Generated by Django 4.2.11 on 2024-04-22 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_invitecoderelation_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='auth_code',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='activated_invite_code',
        ),
        migrations.RemoveField(
            model_name='user',
            name='invite_code',
        ),
        migrations.DeleteModel(
            name='InviteCodeRelation',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
