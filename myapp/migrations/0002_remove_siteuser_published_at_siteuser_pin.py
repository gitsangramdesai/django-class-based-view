# Generated by Django 4.0.6 on 2022-08-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='published_at',
        ),
        migrations.AddField(
            model_name='siteuser',
            name='pin',
            field=models.CharField(default='', max_length=20),
        ),
    ]
