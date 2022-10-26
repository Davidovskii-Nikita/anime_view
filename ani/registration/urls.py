from django.urls import path
from .views import SingUpView, SignInView, ProfileView

urlpatterns = [
    path('signup/',SingUpView.as_view(), name='signup'),
    path('signin/',SignInView.as_view(), name='signin'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]