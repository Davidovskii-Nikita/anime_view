from django.urls import path, include

from blog.views import BlogView, BlogDetailsView

urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<slug:blog_slug>', BlogDetailsView.as_view(), name='blog_details'),
]