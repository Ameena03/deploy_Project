# Generated by Django 3.1.6 on 2021-07-05 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210705_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='p_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_date',
            field=models.CharField(choices=[('2550', '2550'), ('2551', '2551'), ('2552', '2552'), ('2553', '2553'), ('2554', '2554'), ('2555', '2555'), ('2556', '2556'), ('2557', '2557'), ('2558', '2558'), ('2559', '2559'), ('2560', '2560'), ('2561', '2561'), ('2562', '2562'), ('2563', '2563'), ('2564', '2564')], max_length=20),
        ),
    ]