from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView 
)


# Create your views here.
class Login(LoginView):
    template_name='login.html'
    redirect_autheticated_user=True



class Logout(LogoutView):
    next_page = '/'