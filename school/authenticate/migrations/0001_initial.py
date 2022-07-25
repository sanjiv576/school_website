
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(default='', max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10, unique=True)),
                ('image', models.FileField(default='default.jpg', upload_to='static/images/user')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=160)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
