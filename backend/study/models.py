from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class VisibleManager(models.Manager):
    """Менеджер моделей, возвращающий записей с is_visible == True"""

    def get_queryset(self):
        return super().get_queryset().filter(is_visible=True)


class Section(models.Model):
    """Раздел сайта, включающий статьи по одной тематике"""

    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость')

    objects = models.Manager()
    visible = VisibleManager()

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('section', kwargs={'slug': self.slug})


class Article(models.Model):
    """Отдельная статья"""

    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    summary = models.TextField(blank=True, null=True, verbose_name='Краткое содержание')
    text = models.TextField(blank=True, null=True, verbose_name='Текст статьи')
    added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_visible = models.BooleanField(default=True, verbose_name='Видимость')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='articles', verbose_name='Раздел')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='articles',
                             verbose_name='Пользователь')

    objects = models.Manager()
    visible = VisibleManager()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['id']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})
