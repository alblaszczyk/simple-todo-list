"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from todolist.views import main_view, list_view, todo_list_new, todo_list_remove, create_task, remove_task, task_do, done_task

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_view, name="main"),
    url(r'^list/(?P<pk>\d+)/$', list_view, name='list_view'),
    url(r'^new/new_list/$', todo_list_new, name='todo_list_new'),
    url(r'^remove/(?P<pk>\d+)/$', todo_list_remove, name='todo_list_remove'),
    url(r'^(?P<pk>\d+)/task/$', create_task, name='create_task'),
    url(r'^remove/task/(?P<pk>\d+)/$', remove_task, name='remove_task'),
    url(r'^do/task/(?P<pk>\d+)/$', task_do, name='task_do'),
    url(r'^done-task/$', done_task, name='done_task'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
