from django.http import HttpRequest
from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import DetailView

from ani_app.models import Series, Comments, Serials, Categories

from ani_app.forms import CommentsForm
from blog.models import Blog


class ContextMixnin:
    context  = {
    'site_title': 'FIRST_TRY',
    'facebook': 'https://facebook.com',
    'twitter': 'https://tweeter.com',
    'github': 'https://github.com',
    'linkedin': 'https://linkedin.com',
    }


class AnimeWatchingView(ContextMixnin, DetailView):
    model = Series

    template_name = 'anime_whatching/anime-watching.html'
    context_object_name = 'series'
    slug_url_kwarg = 'series_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(AnimeWatchingView, self).get_context_data()
        extra_contex = {
            'serial_title': self.object.serial,
            'ser': Series.objects.filter(serial = self.object.serial),
            'comments': Comments.objects.filter(serial=self.object.serial),
            'form': CommentsForm(),
            'categories': Categories.objects.all(),
        }
        print(self.object.serial)
        contex.update(self.context)
        contex.update(extra_contex)
        return contex

    def post(self, request: HttpRequest,  *args, **kwargs):

        form = CommentsForm(request.POST)

        for field in form:
            print("Field Error:", field.name, field.errors)

        if form.is_valid():
            post_details = form.save(commit=False)
            post_details.author = request.user
            post_details.serial = Serials.objects.get(slug=self.kwargs['serial_slug'])
            post_details.date_published = now()
            #send_mail.delay(request.POST.get('comment.text'))
            form.save()

        return self.get(request=request)
