from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path(r'login', views.user_login, name='login'),
    path(r'logout', views.user_logout, name='logout'),
    path(r'homepage', views.homepage, name='homepage'),
    path(r'register',views.Register.as_view(), name="register")
]