from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User

from ani_app.models import Categories, WithVisitCounter


class Blog(WithVisitCounter, models.Model):

    views = models.IntegerField(
        verbose_name='views',
        default= 0,
    )

    title = models.CharField(
        verbose_name= 'title',
        max_length=50,
    )
    subtitle = models.CharField(
        verbose_name= 'subtitle',
        max_length=50,
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date_published',
        null=True
    )
    text = models.TextField(
        verbose_name='text',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='author'
    )
    image = models.ImageField(
        upload_to='blog/'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='is_published', null=True
    )
    category = models.ManyToManyField(
        Categories,
        blank= True, null= True,
        verbose_name= 'category'
    )

    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog', kwargs={'blog_slug': self.slug})

    class Meta:
        db_table = 'blog_post'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('date_published','is_published',)

