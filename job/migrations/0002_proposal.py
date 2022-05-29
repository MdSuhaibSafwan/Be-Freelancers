# Generated by Django 4.0.4 on 2022-05-28 10:58

import base_lib.model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_developer_client'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.UUIDField(default=base_lib.model.create_uuid, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.developer')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='job.job')),
                ('job_question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.jobquestion')),
            ],
            options={
                'unique_together': {('job_question', 'developer'), ('job', 'developer')},
            },
        ),
    ]
