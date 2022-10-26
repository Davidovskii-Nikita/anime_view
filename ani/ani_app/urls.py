from django.urls import path, include
from .views import IndexView, AnimeDetailsView, AnimeWatchingView, CategoriesView, BlogView, BlogDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('anime_details', AnimeDetailsView.as_view(), name='anime_details'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog_details', BlogDetailsView.as_view(), name='blog_details'),
    path('anime_watching', AnimeWatchingView.as_view(), name='anime_watching'),
    path('<slug:serial_slug>', AnimeDetailsView.as_view(), name='anime_details_slug'),
]