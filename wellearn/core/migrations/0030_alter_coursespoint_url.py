# Generated by Django 4.2.2 on 2023-06-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_alter_settings_worktime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursespoint',
            name='url',
            field=models.CharField(default='about', max_length=50, verbose_name='Url'),
        ),
    ]