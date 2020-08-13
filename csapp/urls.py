from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'csapp'

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.cs_signin, name='signin'),
    path('registrar/', views.cs_signup, name='signup'),
    path('perfil/', views.cs_profile, name='profile'),
    path('logout/', views.cs_exit, name='exit'),
    path('redefinir-senha/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change-password'),
    path('buscar/', views.cs_search, name='search'),
]