# Generated by Django 4.2.1 on 2023-05-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_newsletters'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='rights',
            field=models.CharField(default='', max_length=50),
        ),
    ]
