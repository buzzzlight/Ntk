# Generated by Django 3.2.13 on 2022-11-29 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20221128_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='boj_username',
            new_name='boj_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='git_username',
            new_name='git_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='detail_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_email_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_phone_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
