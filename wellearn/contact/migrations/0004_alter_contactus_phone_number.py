# Generated by Django 4.2.1 on 2023-05-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone Num'),
        ),
    ]
