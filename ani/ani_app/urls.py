from django.urls import path, include
from .views import IndexView, AnimeDetailsView, CategoriesView, BlogView, BlogDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('<slug:category_slug>', CategoriesView.as_view(), name='categories'),
    path('<slug:serial_slug>/', AnimeDetailsView.as_view(), name='anime_details_slug'),
]