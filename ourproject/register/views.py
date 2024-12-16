from django.shortcuts import render, redirect
from .forms import  RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
# Create your views here.
def register(response):
  if response.method =="POST":
    form =  RegisterForm(response.POST)
    if form.is_valid():
      form.save()
      return redirect("login")

  else:
    form =  RegisterForm()

  return render(response, "register/register.html", {"form":form})

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('home')
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})

def logout(response):
  logout(response)
  return redirect("login")