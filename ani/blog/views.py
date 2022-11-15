from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from ani_app.views import BlogView
from blog.models import Blog


class ContextMixnin:
    context  = {
    'site_title': 'FIRST_TRY',
    'facebook': 'https://facebook.com',
    'twitter': 'https://tweeter.com',
    'github': 'https://github.com',
    'linkedin': 'https://linkedin.com',
    }

class BlogView(ContextMixnin, TemplateView):
    template_name = 'blog/blog.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(BlogView, self).get_context_data()
        extra_context = {
                'posts':Blog.objects.filter(is_published = True)
        }
        contex.update(self.context)
        contex.update(extra_context)
        return contex


class BlogDetailsView(ContextMixnin, DetailView):

    model = Blog
    template_name = 'blog/blog-details.html'

    context_object_name = 'blog'
    slug_url_kwarg = 'blog_slug'


    def get_queryset(self):
        return Blog.objects.filter(is_published = True)

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(BlogDetailsView, self).get_context_data()
        contex.update(self.context)
        return contex

