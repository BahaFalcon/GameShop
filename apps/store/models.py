from django.db import models
from ckeditor.fields import RichTextField


class Genre(models.Model):
    """Модель жанров"""
    title = models.CharField('Жанр', max_length=50)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Game(models.Model):
    """Модель игры"""
    name = models.CharField('Название', max_length=255)
    image = models.ImageField('Изображение', upload_to='image/')
    genre = models.ManyToManyField(Genre, related_name='games', verbose_name='Жанры')
    description = RichTextField('Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return self.name




