"""new_migration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url , re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('articles.urls')),
    # re_path(r'^articles/',articles.urls),
    
    re_path(r'^home/$',views.home),
    # path('',views.home,name='home'), using '' going to 127.0.0.1.:8000
    # path('home/',views.home,name='home'), using path pointing to location path url
    
    ## AUTH URLS
    re_path(r'^accounts/login/$',views.login),
    re_path(r'^accounts/auth/$',views.auth_view),
    re_path(r'^accounts/logout/$',views.logout),
    re_path(r'^accounts/loggedin/$',views.loggedin),
    re_path(r'^accounts/invalidlogin/$',views.invalidlogin),
    re_path(r'^accounts/register/$',views.register_user),
    re_path(r'^accounts/register_success/$',views.register_success),
    
    
    
    
]
