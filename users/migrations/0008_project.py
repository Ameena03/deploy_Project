# Generated by Django 3.1.6 on 2021-07-04 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.TextField(max_length=500)),
                ('p_date', models.DateTimeField(auto_now_add=True)),
                ('p_abstract', models.TextField(max_length=500)),
                ('f_pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('p_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
                ('p_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='users.category')),
            ],
        ),
    ]
