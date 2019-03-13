from django.urls import path
from register import views

urlpatterns = [
    #http://127.0.0.1:8000/account/ 这两个url指向都是注册页面
    path('', views.register, name='register'),
    path('register/',views.register,name = 'register'),
]
