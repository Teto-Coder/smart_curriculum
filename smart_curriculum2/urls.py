"""smart_curriculum2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from curriculum.views import *
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),  
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^logout/',logout, name='logout'),
    url(r'^index/',index, name='index'),
    url(r'^Register/',Register, name='Register'),
    url(r'^Edit/',Edit, name='Edit'),
    url(r'^Finish/', Finish, name='Finish'),
    url(r'^change_course/', change_course, name='change_course'),
    url(r'^courses/',courses, name='courses'),
    url(r'^courses_info/',courses_info, name='courses_info'),
   
     
]
