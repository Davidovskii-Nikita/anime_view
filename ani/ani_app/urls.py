from django.urls import path, include
from .views import IndexView, AnimeDetailsView, CategoriesView, BlogView, BlogDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('blog', BlogView.as_view(), name='blog'),
    path('blog_details', BlogDetailsView.as_view(), name='blog_details'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('<slug:serial_slug>/', AnimeDetailsView.as_view(), name='anime_details_slug'),
]