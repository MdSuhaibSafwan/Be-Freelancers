# Generated by Django 4.0.4 on 2022-05-28 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]