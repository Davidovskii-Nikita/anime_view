from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Serials, Comments


def main(request: HttpResponse):
    return render(request, 'ani_app/index.html')



class ContextMixnin:
    context  = {
    'site_title': 'FIRST_TRY',
    'facebook': 'https://facebook.com',
    'twitter': 'https://tweeter.com',
    'github': 'https://github.com',
    'linkedin': 'https://linkedin.com',
    }


class IndexView(ContextMixnin, TemplateView):
    template_name = 'ani_app/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(IndexView, self).get_context_data()
        contex.update(self.context)
        return contex



class AnimeDetailsView(ContextMixnin, DetailView):
    model = Serials
    template_name = 'ani_app/anime-details.html'
    context_object_name = 'serial'
    slug_url_kwarg = 'serial_slug'
    extra_context = {'comments': Comments.objects.filter(is_published=True).order_by('date_published'),
                     'serials': Serials.objects.filter(is_published=True).order_by('date_published')
                     }

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(AnimeDetailsView, self).get_context_data()
        contex.update(self.context)
        return contex


class AnimeWatchingView(ContextMixnin, TemplateView):

    template_name = 'ani_app/anime-watching.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(AnimeWatchingView, self).get_context_data()
        contex.update(self.context)
        return contex



class CategoriesView(ContextMixnin, ListView):
    model = Serials
    template_name = 'ani_app/categories.html'
    context_object_name = 'serials'

    def get_queryset(self):
        return Serials.objects.filter(is_published=True).order_by('date_published')

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(CategoriesView, self).get_context_data()
        contex.update(self.context)
        return contex

class  BlogView(ContextMixnin, TemplateView):

    template_name = 'ani_app/blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(   BlogView, self).get_context_data()
        contex.update(self.context)
        return contex


class BlogDetailsView(ContextMixnin, TemplateView):
    template_name = 'ani_app/blog-details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(BlogDetailsView, self).get_context_data()
        contex.update(self.context)
        return contex