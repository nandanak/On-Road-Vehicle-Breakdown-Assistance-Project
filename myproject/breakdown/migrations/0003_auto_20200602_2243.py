# Generated by Django 3.0.6 on 2020-06-02 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breakdown', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='hi'),
        ),
        migrations.AddField(
            model_name='profile',
            name='special',
            field=models.CharField(default='nothing', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='hi'),
        ),
        migrations.AddField(
            model_name='user',
            name='special',
            field=models.CharField(default='nothing', max_length=100),
        ),
    ]
