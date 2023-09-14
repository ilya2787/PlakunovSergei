# Generated by Django 4.1.7 on 2023-04-14 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Темы',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.CharField(max_length=300, verbose_name='Краткое описание')),
                ('content_big', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('image', models.ImageField(upload_to='image/%Y', verbose_name='Изображение на зоголовок')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='MyBlog.topicpost', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Photo_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='image/post/%Y', verbose_name='Изображение для поста')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyBlog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Изоброжения',
                'verbose_name_plural': 'Изоброжения для поста',
                'ordering': ['post'],
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='ip-адрес')),
                ('pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyBlog.post', verbose_name='Публикация')),
            ],
        ),
    ]