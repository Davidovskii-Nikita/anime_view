from django.utils.timezone import now

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from .models import Serials, Comments, Series, Categories
from .forms import CommentsForm
from .tasks import send_mail


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
        extra_context = {
                        'categories': Categories.objects.all(),
                        'serials': Serials.objects.filter(is_published = True)
                         }
        contex.update(extra_context)
        contex.update(self.context)
        return contex



class AnimeDetailsView(ContextMixnin, DetailView):

    model = Serials
    template_name = 'ani_app/anime-details.html'
    context_object_name = 'serial'
    slug_url_kwarg = 'serial_slug'


    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(AnimeDetailsView, self).get_context_data()
        extra_context = {
                         'comments': Comments.objects.filter(serial = self.object),
                         'serials': Serials.objects.filter().order_by('date_published'),
                         'series': Series.objects.filter(serial=self.object)[0],
                         'form': CommentsForm(),
                         'categories': Categories.objects.all()
                         }
        contex.update(self.context)
        contex.update(extra_context)
        return contex

    def post(self, request: HttpRequest,  *args, **kwargs):

        form = CommentsForm(request.POST)

        for field in form:
            print("Field Error:", field.name, field.errors)

        if form.is_valid():

            post_details = form.save(commit=False)
            post_details.author = request.user
            post_details.serial =Serials.objects.get(slug=self.kwargs['serial_slug'])
            post_details.date_published = now()
            #send_mail.delay(request.POST.get('comment.text'))
            form.save()
            comments = Comments.objects.filter(serial=Serials.objects.get(slug=self.kwargs['serial_slug']))
            post_details.serial.count_comments = len(comments)
            post_details.serial.save()

        return self.get(request=request)


class CategoriesView(ContextMixnin, DetailView):
    model = Categories
    template_name = 'ani_app/categories.html'
    context_object_name = 'categories'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(CategoriesView, self).get_context_data()
        last_comments = []
        print(type(Comments.objects.all()))
        for comment in Comments.objects.all():
            if (now() - comment.date_published).total_seconds() < 3600:
                last_comments.append(comment)
        extra_context = {
                         'categories' : Categories.objects.all(),
                         'cat': self.object,
                         'serials': Serials.objects.filter(category =self.object),
                         'last_comments': last_comments,
                         }
        contex.update(extra_context)
        contex.update(self.context)
        return contex

class BlogView(ContextMixnin, TemplateView):

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