# Generated by Django 4.0.5 on 2022-07-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='', max_length=10),
        ),
    ]
