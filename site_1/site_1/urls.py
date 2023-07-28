"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:

Function views # 이 방법을 제일 많이 사용할 예정
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    
Including another URLconf (URL 권한 위임) 
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lotto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #$ path('', views.index), # lotto > views.py 파일의 index() 함수 호출
    path('hello/', views.hello, name='hello_main'), # lotto > views.py 파일의 hello() 함수 호출, name은 별명이다
    path('lotto/', views.index, name='index'), # http://127.0.0.1:8000/lotto/
    path('lotto/new/', views.post, name='new_lotto'),
    path('lotto/<int:lottokey>/detail', views.detail, name='detail'),
]