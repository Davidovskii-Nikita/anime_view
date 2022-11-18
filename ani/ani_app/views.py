from django.db.models import Max
from django.utils.timezone import now

from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Blog
from .models import Serials, Comments, Series, Categories
from .forms import CommentsForm

from django.views.generic.detail import SingleObjectMixin


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

class ContextMixnin_With_Wisitors(SingleObjectMixin):

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if str(self.request.user) != 'AnonymousUser':
            obj.visitors.add(self.request.user)
            return obj
        else:
            return obj

    def get_context_data(self, *args, **kwargs):
        cd = super().get_context_data(*args, **kwargs)
        cd['visits'] = self.object.visitors.count()
        return cd

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
                        'serials': Serials.objects.filter(is_published = True).order_by('-views').annotate(Max('views'))[:3],
                        'blogs':Blog.objects.all().order_by('-views').annotate(Max('views'))[:3],
                        'comments': Comments.objects.all()[::-1][:3],
                        'trend_now': Serials.objects.filter(category__title = "Trending Now")[:6],
                        'trend_now_slug': Categories.objects.filter(title = "Trending Now")[0].slug,
                        'top_viws': Serials.objects.filter(category__title = "Top views")[:6],
                        'top_viws_slug': Categories.objects.filter(title="Top views")[0].slug,
                        'popular_show': Serials.objects.filter(category__title = "Popular show")[:6],
                        'popular_show_slug': Categories.objects.filter(title="Popular show")[0].slug,
                         }
        # print(extra_context['trend_now_slug'][0].slug)
        contex.update(extra_context)
        contex.update(self.context)
        return contex



class AnimeDetailsView(ContextMixnin_With_Wisitors, DetailView):

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
                         'categories': Categories.objects.all(),
                         'serial': Serials.objects.get(title = self.object),
                         'blogs': Blog.objects.all()[:3]
                         }
        contex.update(self.context)

        print(self.request.user)

        serial = extra_context['serial']
        serial.views = contex['visits']
        serial.save(update_fields=['views'])

        contex.update(extra_context)

        return contex

    def post(self, request: HttpRequest,  *args, **kwargs):
        global list_of_comm_id

        form = CommentsForm(request.POST)

        for field in form:
            print("Field Error:", field.name, field.errors)
        print(request.META.get('HTTP_X_FORWARDED_FOR'))
        if form.is_valid():
            post_details = form.save(commit=False)
            post_details.author = request.user
            post_details.serial = Serials.objects.get(slug=self.kwargs['serial_slug'])
            post_details.date_published = now()
            #send_mail.delay(request.POST.get('comment.text'))
            form.save()
            comments = Comments.objects.filter(serial=Serials.objects.get(slug=self.kwargs['serial_slug']))
            post_details.serial.count_comments = len(comments)
            post_details.serial.save()

        return self.get(request=request)


class CategoriesView(ContextMixnin, ListView):
    model = Categories
    template_name = 'ani_app/categories.html'
    context_object_name = 'categories'
    slug_url_kwarg = 'category_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(CategoriesView, self).get_context_data()

        extra_context = {
                         'categories' : Categories.objects.all(),
                         'cat': Categories.objects.get(slug = self.kwargs['category_slug']),
                         'serials': Serials.objects.filter(category__slug =self.kwargs['category_slug']),
                         'comments': Comments.objects.all()[::-1][:3],
                         'blogs': Blog.objects.all().order_by('-views').annotate(Max('views'))[:3]
                         }
        contex.update(extra_context)
        contex.update(self.context)
        return contex


class BlogView(ContextMixnin, TemplateView):

    template_name = 'ani_app/blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super( BlogView, self).get_context_data()
        contex.update(self.context)
        return contex


class BlogDetailsView(ContextMixnin, TemplateView):
    template_name = 'ani_app/blog-details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(BlogDetailsView, self).get_context_data()
        contex.update(self.context)
        return contex


class Categories_lsitView(ContextMixnin, ListView):
    model = Categories
    template_name = 'ani_app/categories_list.html'
    context_object_name = 'categories_list'
    paginate_by = 2

    def get_context_data(self, *, object_list = None, ** kwargs):
        context = super(Categories_lsitView, self).get_context_data()
        context['categories'] = Categories.objects.all()
        context['comments'] = Comments.objects.all()[::-1][:3]
        context['blogs'] =Blog.objects.all().order_by('-views').annotate(Max('views'))[:3]
        context.update(self.context)
        return context