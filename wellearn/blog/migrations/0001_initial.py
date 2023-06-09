# Generated by Django 4.2.1 on 2023-05-18 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='AuthorsIMG', verbose_name='Image')),
                ('age', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Title')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('published_at', models.DateField(verbose_name='Published_at')),
                ('blog_image', models.ImageField(upload_to='BlogIMG', verbose_name='Image')),
                ('slug', models.SlugField(unique=True)),
                ('blog_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_posts', to='blog.blogauthor')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
