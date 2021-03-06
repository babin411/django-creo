# Generated by Django 2.1.2 on 2018-11-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creo', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=264, unique=True)),
                ('first_name', models.CharField(max_length=264)),
                ('last_name', models.CharField(max_length=264)),
                ('email_id', models.EmailField(max_length=264, unique=True)),
                ('date_of_birth', models.DateTimeField(verbose_name='date of birth')),
            ],
        ),
    ]
