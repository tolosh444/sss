# Generated by Django 4.2.1 on 2023-05-14 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_delete_getintouchpoint'),
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
        migrations.AlterField(
            model_name='settings',
            name='adress',
            field=models.CharField(max_length=100, verbose_name='Adress'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(upload_to='Settings', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='phone',
            field=models.IntegerField(default=1, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='title',
            field=models.CharField(default='Title', max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='worktime',
            field=models.CharField(default='', max_length=25, verbose_name='Worktime'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='year',
            field=models.CharField(default='', max_length=10, verbose_name='Year'),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('published_at', models.DateTimeField(verbose_name='Published_at')),
                ('blog_image', models.ImageField(upload_to='BlogIMG', verbose_name='Image')),
                ('slug', models.SlugField(unique=True)),
                ('blog_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_posts', to='core.blogauthor')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
