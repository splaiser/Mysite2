from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
#from .forms import AuthUserForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def contacts(request):
    return render(request, 'main/contacts.html')
def userlog(request):
    return render(request, 'main/userlog.html')
#class MysiteLoginView(LoginView):
    #template_name = 'userlog.html'
    #form_class = AuthUserForm
    #success_url = reversed('edit_page')
