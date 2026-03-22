from django.db import models
from django.contrib.auth import get_user_model

from .constants import TITLE_MAX_LEN

User = get_user_model()


class PublCreatModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано', default=True, help_text='Снимите галочку, '
        'чтобы скрыть публикацию.')
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class Category(PublCreatModel):
    title = models.CharField('Заголовок', max_length=TITLE_MAX_LEN)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', unique=True,
                            help_text='Идентификатор страницы для URL; '
                            'разрешены символы латиницы, цифры, дефис '
                            'и подчёркивание.')

    class Meta(PublCreatModel.Meta):
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(PublCreatModel):
    name = models.CharField('Название места', max_length=TITLE_MAX_LEN)

    class Meta(PublCreatModel.Meta):
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(PublCreatModel):
    title = models.CharField('Заголовок', max_length=TITLE_MAX_LEN)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации', help_text='Если установить дату и '
        'время в будущем — можно делать отложенные публикации.')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор публикации')
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name='Местоположение')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=False, null=True,
        verbose_name='Категория')

    class Meta(PublCreatModel.Meta):
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']
