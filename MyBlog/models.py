from django.db import models

class Post(models.Model):
    """Основная структура поста"""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.CharField(max_length=300, verbose_name="Краткое описание")
    content_big = models.TextField(null=True, blank=True, verbose_name="Описание")
    topic = models.ForeignKey('TopicPost', null=True, on_delete=models.PROTECT, verbose_name="Тема")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    image = models.ImageField(upload_to='image/%Y', verbose_name="Изображение на зоголовок")


    class Meta:
        verbose_name_plural = "Посты"
        verbose_name = "Пост"
        ordering = ['-published']


class Photo_post(models.Model):
    """Фотографии для конкретного поста"""
    images = models.ImageField(upload_to='image/post/%Y', verbose_name="Изображение для поста")
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, verbose_name="Пост")

    class Meta:
        verbose_name_plural = "Изоброжения для поста"
        verbose_name = "Изоброжения"
        ordering = ['post']


class TopicPost(models.Model):
    """Тема публикаций"""
    name = models.CharField(max_length=50, db_index=True, verbose_name="Название")

    def __str__(self):
       return self.name

    class Meta:
        verbose_name_plural = "Темы"
        verbose_name = "Тема"
        ordering = ['-id']

class Likes(models.Model):
    """лайки"""
    ip = models.CharField(max_length=100, verbose_name="ip-адрес")
    pos = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE)