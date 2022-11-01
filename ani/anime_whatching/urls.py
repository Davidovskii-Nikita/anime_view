from django.urls import path

from .views import AnimeWatchingView

urlpatterns = [
    path('<slug:serial_slug>/<slug:series_slug>', AnimeWatchingView.as_view(), name='anime_watching_slug')
]