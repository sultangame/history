from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Новый автор")
    bio = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Автор"

    def __str__(self):
        return self.user.username


class Category(models.Model):
    category = models.CharField(max_length=255, verbose_name="категория")
    class Meta:
        verbose_name = "Категории"
    
    def __str__(self) -> str:
        return self.category
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=255, unique=True, verbose_name="Загаловок")
    image = ThumbnailerImageField(verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Слаг")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    body = models.TextField(verbose_name="Текст")
    crated = models.DateTimeField(default=timezone.now, verbose_name="созданно")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="обновлено")
    publish = models.DateTimeField(auto_now=True, verbose_name="опубликованно")
    status = models.CharField(max_length=2, 
                              choices=Status.choices,
                              default=Status.DRAFT,
                              verbose_name="Статус")
    objects = models.Manager() 
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name = "Посты"
    
    def __str__(self):
        return self.title
    