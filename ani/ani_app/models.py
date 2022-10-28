
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import now



class Comments (models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author'
    )

    serial = models.ForeignKey(
        'Serials',
        on_delete=models.PROTECT,
        blank=True, null=True,
        verbose_name='serial'
    )

    text = models.TextField(
        max_length=250,
        verbose_name = 'comment'
    )

    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date_published'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='is_published'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('date_published', )


class Serials(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='title',
    )
    subtitle = models.CharField(
        max_length=60,
        verbose_name=' subtitle'
    )
    type = models.CharField(
        max_length=20,
        verbose_name='type'
    )
    studio = models.CharField(
        max_length=20,
        verbose_name='studio'
    )
    date_aried = models.DateTimeField(
        verbose_name='date_aried'
    )
    status = models.CharField(  # переделать в Boolian
        max_length=20,
        verbose_name='status',
    )
    genre = models.CharField(
        max_length=30,
        verbose_name='genre'
    )
    rating = models.CharField(
        max_length=30,
        verbose_name='rating'
    )
    duration = models.CharField(
        max_length=30,
        verbose_name='duration'
    )
    quality = models.CharField(
        max_length=30,
        verbose_name='quality'
    )
    views = models.IntegerField(
        verbose_name='views'
    )
    image = models.ImageField(
        upload_to='serials_image/',
        verbose_name='image'
    )
    text_description = models.TextField(
        verbose_name='text_description'
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date published'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='is published'
    )

    pk_comm = models.ForeignKey(
        Comments,
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name='pk_comm'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('serials', kwargs={'serials_slug': self.slug})

    class Meta:
        db_table = 'anime_serials'
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
        ordering = ('date_published', 'genre',)