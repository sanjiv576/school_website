# Generated by Django 4.0.5 on 2022-07-22 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_rename_user_userinfo_alter_userinfo_table'),
        ('user', '0006_alter_notice_vacancy_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('intro_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('intro_title', models.CharField(max_length=30)),
                ('intro_image', models.FileField(default='default.jpeg', upload_to='static/images/intro')),
                ('intro_description', models.TextField(max_length=200)),
                ('user_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='authenticate.userinfo')),
            ],
            options={
                'db_table': 'Intro',
            },
        ),
    ]