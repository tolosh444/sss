# Generated by Django 4.2.2 on 2023-06-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.TextField(blank=True, choices=[(None, 'Not chosen'), ('M', 'Male'), ('F', 'Female')], null=True, verbose_name='Gender'),
        ),
    ]
