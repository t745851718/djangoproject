from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # 登录页面
    path(r'login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # 登出页面
    path(r'logout/', auth_views.LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),

    # 注册页面
    path(r'register/', views.register, name='register'),
]