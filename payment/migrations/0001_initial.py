# Generated by Django 4.0.4 on 2022-05-29 08:36

import base_lib.model
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0004_jobrating_jobinvite'),
        ('account', '0004_developer_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='BkashToDeveloperPayment',
            fields=[
                ('id', models.UUIDField(default=base_lib.model.create_uuid, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('pending', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='bkash/transaction/images/developer')),
                ('bkash_transaction_number', models.CharField(max_length=500, null=True, unique=True)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bkash_history', to='account.developer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BkashClientPayment',
            fields=[
                ('id', models.UUIDField(default=base_lib.model.create_uuid, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('transaction_number', models.CharField(editable=False, max_length=500, unique=True)),
                ('bkash_transaction_number', models.CharField(max_length=500, unique=True)),
                ('image1', models.ImageField(upload_to='bkash/transaction/images/client')),
                ('image2', models.ImageField(null=True, upload_to='bkash/transaction/images')),
                ('pending', models.BooleanField(default=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.client')),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.developer')),
                ('job', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='job.job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]