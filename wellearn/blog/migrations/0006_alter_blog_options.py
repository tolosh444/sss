# Generated by Django 4.2.2 on 2023-06-05 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_published_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-published_at'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]
