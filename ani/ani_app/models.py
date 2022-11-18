from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.timezone import now


class WithVisitCounter(models.Model):

    visitors = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='%(model_name)s_visits' 
    )

    class Meta:
        abstract = True


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
        verbose_name = 'comment', null=True
    )

    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date_published', null=True
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='is_published', null=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('date_published', )

class Categories (models.Model):

    title = models.CharField(
        max_length=50,
        verbose_name='title',
        unique=True
    )
    count = models.IntegerField(
        verbose_name='count',
        default=0
    )

    serial = models.ManyToManyField(
        'Serials',
        blank=True, null=True,
        verbose_name='serials'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('categories', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

class Serials( WithVisitCounter, models.Model):

    category = models.ManyToManyField(
        Categories,
        blank=True, null=True,
        verbose_name='category'
    )

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

    count_comments = models.IntegerField(
        default= 0,
        verbose_name= 'count_comments'
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


class Series(models.Model):

    title = models.CharField(
        max_length= 30,
        verbose_name='title',
        blank=True, null=True,
    )
    season = models.IntegerField(
        verbose_name='season',
        null=True
    )
    serial = models.ForeignKey(
        Serials,
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name='serial'
    )
    image = models.ImageField(
        upload_to='series_image/',
        verbose_name='image',
        null=True
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date published'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )
    is_published = models.BooleanField (
        default=False,
        verbose_name='is_published'
    )

    video = models.FileField(
        blank= True, null=True,
        verbose_name='video'
    )


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('series', kwargs={'series_slug': self.slug})

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
        ordering = ('date_published', )