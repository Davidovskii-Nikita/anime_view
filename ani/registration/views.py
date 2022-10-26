from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import SignUpForm, SignInForm


class SingUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('signin')
    template_name = 'registration/signup.html'

class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('main')

class ProfileView(LoginRequiredMixin, View):
    template_name = 'registration/profile.html'
    login_url = '/login/'

    def get_queryset(self):
        return User.objects.filter(username = self.request.user)[0]

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

