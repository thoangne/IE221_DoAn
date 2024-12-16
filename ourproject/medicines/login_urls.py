from django.urls import path
from .views import *
app_name = 'medicines'

urlpatterns = [
  path('', LoginView.register_view, name='register'),
  path('register/', LoginView.register_view, name='register'),
  path('login/', LoginView.login_view, name='login'),
  path('logout/', LoginView.logout_view, name='logout'),
]