from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.detail import SingleObjectMixin

from ani_app.models import Categories
from ani_app.views import BlogView
from blog.models import Blog




class ContextMixnin:

    context  = {
    'site_title': 'FIRST_TRY',
    'facebook': 'https://facebook.com',
    'twitter': 'https://tweeter.com',
    'pinterest': 'https://www.pinterest.com/',
    'linkedin': 'https://linkedin.com',
    }

class ContextMixnin_With_Wisitors(SingleObjectMixin, ContextMixnin):

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        obj.visitors.add(self.request.user)
        return obj

    def get_context_data(self, *args, **kwargs):
        cd = super().get_context_data(*args, **kwargs)
        cd['visits'] = self.object.visitors.count()
        return cd



class BlogView(ContextMixnin,ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(BlogView, self).get_context_data()
        extra_context = {
                'posts':Blog.objects.filter(is_published = True),
                'categories': Categories.objects.all(),
        }

        contex.update(self.context)
        contex.update(extra_context)
        return contex


def get_next_blog(slug_list, slug):
    x = 0
    y = 0
    for blog in slug_list:
        x = x + 1
        if blog['slug'] == slug:
            y = x - 1
    if y == 0:
        previous_index = slug_list[0]
        next_index = slug_list[1]
    elif y + 1 == len(slug_list):
        previous_index = slug_list[len(slug_list) - 2]
        next_index = slug_list[len(slug_list) - 1]
    else:
        previous_index = slug_list[y - 1]
        next_index = slug_list[y + 1]
    x = 0
    return previous_index['slug'], next_index['slug']



class BlogDetailsView(ContextMixnin_With_Wisitors, DetailView):
    model = Blog
    template_name = 'blog/blog-details.html'
    context_object_name = 'blog'
    slug_url_kwarg = 'blog_slug'
    def get_queryset(self):
        return Blog.objects.filter(is_published = True)
    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super(BlogDetailsView, self).get_context_data()
        contex['categories'] = Categories.objects.all()
        # contex['blog'] = Blog.objects.filter(is_published = True)

        this_blog = Blog.objects.filter(is_published = True).values('slug')
        p,n= get_next_blog(this_blog,self.kwargs['blog_slug'])
        contex['previous_index'] = p
        contex['next_index'] = n

        contex['previous_title']=Blog.objects.filter(slug = p)
        contex['next_title']= Blog.objects.filter(slug =n)
        print(contex['next_title'])
        blog = Blog.objects.get(title = self.object)
        blog.views = contex['visits']
        blog.save(update_fields=['views'])

        contex.update(self.context)
        return contex

