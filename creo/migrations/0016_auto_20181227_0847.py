# Generated by Django 2.1.2 on 2018-12-27 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creo', '0015_commentpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentpost',
            old_name='content',
            new_name='comment',
        ),
    ]