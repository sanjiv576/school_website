# Generated by Django 4.0.5 on 2022-07-22 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_rename_user_userinfo_alter_userinfo_table'),
        ('user', '0007_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='user_id',
            field=models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='authenticate.userinfo'),
        ),
    ]
