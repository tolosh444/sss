# Generated by Django 4.2.1 on 2023-05-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_settings_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='worktime',
            field=models.CharField(default='', max_length=50, verbose_name='Worktime'),
        ),
    ]
