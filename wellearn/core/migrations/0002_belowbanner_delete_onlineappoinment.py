# Generated by Django 4.2.1 on 2023-05-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BelowBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('image', models.ImageField(upload_to='Below_Banner', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'BelowBanner',
                'verbose_name_plural': 'BelowBanner',
            },
        ),
        migrations.DeleteModel(
            name='OnlineAppoinment',
        ),
    ]
