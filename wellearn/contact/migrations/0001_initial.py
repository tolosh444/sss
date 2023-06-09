# Generated by Django 4.2.1 on 2023-05-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='contactPage/images', verbose_name='banner')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Phone')),
                ('optional_phone_number', models.CharField(blank=True, help_text='Ehtiyac olarsa ikinci telefon üçündür, məcburi deyil', max_length=255, null=True, verbose_name='Additional number')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('title', models.CharField(default='Contact Us', max_length=255, verbose_name='Title')),
                ('text', models.TextField(blank=True, null=True, verbose_name='text')),
                ('map_src', models.CharField(blank=True, max_length=500, null=True, verbose_name='Map source')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
