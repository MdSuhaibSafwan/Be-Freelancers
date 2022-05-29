# Generated by Django 4.0.4 on 2022-05-29 08:18

import base_lib.model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_developer_client'),
        ('gig', '0001_initial'),
        ('job', '0004_jobrating_jobinvite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.UUIDField(default=base_lib.model.create_uuid, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.client')),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.developer')),
                ('gig', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gig_contracts', to='gig.gig')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_contracts', to='job.job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
