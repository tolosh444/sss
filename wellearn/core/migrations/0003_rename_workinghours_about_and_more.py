# Generated by Django 4.2.1 on 2023-05-09 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_belowbanner_delete_onlineappoinment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkingHours',
            new_name='About',
        ),
        migrations.RenameModel(
            old_name='WorkingHoursPoint',
            new_name='AboutPoint',
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='aboutpoint',
            options={'verbose_name': 'AboutPoint', 'verbose_name_plural': 'AboutPoints'},
        ),
    ]