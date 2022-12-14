# Generated by Django 4.0.6 on 2022-08-03 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('addressLine1', models.CharField(max_length=500)),
                ('addressLine2', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=255)),
                ('dob', models.DateField()),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('country', models.IntegerField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=100)),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'siteuser',
            },
        ),
    ]
