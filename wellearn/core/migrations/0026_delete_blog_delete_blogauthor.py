# Generated by Django 4.2.1 on 2023-05-18 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_blog_published_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='BlogAuthor',
        ),
    ]