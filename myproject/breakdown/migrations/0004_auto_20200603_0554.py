# Generated by Django 3.0.6 on 2020-06-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0003_auto_20200602_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
