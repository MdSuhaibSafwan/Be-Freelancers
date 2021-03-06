# Generated by Django 4.0.4 on 2022-05-28 10:52

import base_lib.model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_developer_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=base_lib.model.create_uuid, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('open', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('project_type', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='account.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobQuestion',
            fields=[
                ('id', models.UUIDField(default=base_lib.model.create_uuid, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=300)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='job.job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
