"""django_todo URL Configuration

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
from django.urls import path, re_path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Using regular expression
    re_path(r'^$', views.say_hello, name='homere'),
    # Using function view
    path('test', views.say_hello, name='homefv'),
    # Render html file see view
    path('list', views.get_todo_list, name='todo_list.html'),
    path('add', views.create_an_item),
    re_path(r'^edit/(?P<id>\d+)$', views.edit_an_item),
    re_path(r'^toggle/(?P<id>\d+)$', views.toggle_status)
]
