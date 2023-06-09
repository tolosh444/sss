# Generated by Django 4.2.1 on 2023-05-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_delete_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Full_name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Text')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Num')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
            options={
                'verbose_name': 'Contact us',
                'verbose_name_plural': 'Contacts us',
            },
        ),
    ]
