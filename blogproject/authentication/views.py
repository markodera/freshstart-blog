from django.shortcuts import render,redirect
from .forms import CustomAuthenticationform, CustomUserForm, ProfileUpdateForm
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.


class CustomSignUpView(CreateView):
    form_class = CustomUserForm
    template_name = "authentication/signup.html"
    success_url = reverse_lazy("authentication:profile_update")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileUpdateView(UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'registration/profile_update.html'
    success_url = '/profile/'

    def get_object(self):
        return self.request.user
    
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationform
    template_name = 'authentication/login.html'
    success_url = '/'

class ProfileView(DetailView):
    template_name = 'authentication/profile.html'
    def get_object(self):
        return self.request.user
    
def logout_view(request):
    logout(request)
    return redirect("authentication:login")
