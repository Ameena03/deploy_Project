# Generated by Django 3.1.6 on 2021-08-08 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210808_1043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='count_sold',
            new_name='count_download',
        ),
    ]
