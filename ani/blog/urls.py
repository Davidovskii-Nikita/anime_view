from django.urls import path, include
from rest_framework import routers

from blog.views import BlogView, BlogDetailsView, BlogApiView

router = routers.SimpleRouter()
router.register(r'',BlogApiView)
urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/api/v1/', include(router.urls)),
    path('blog/<slug:blog_slug>', BlogDetailsView.as_view(), name='blog_details'),
]