from django.urls import path, include

from users import views

app_name = 'users'

urlpatterns = [
    # 包含默认的身份验证 URL
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
]
