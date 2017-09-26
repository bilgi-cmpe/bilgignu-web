"""bilgignuweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from rest_framework.authtoken import views as drf_views

from blog.views import HomeView, DetailView, CategoryView
from arcade.views import ArcadeView, MachineListView, MachineUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^yazi/(?P<pattern>.*)$', DetailView.as_view()),
    url(r'^cocuklaricinoyna$/', ArcadeView.as_view(), name='arcade'),
    url(r'^api/arcade/all/$', MachineListView.as_view()),
    url(r'^api/arcade/(?P<pk>[0-9]+)/$', MachineUpdateView.as_view()),
    url(r'^kategori/(?P<pattern>.*)/$', CategoryView.as_view()),
    url(r'^get_auth_token/$', drf_views.obtain_auth_token, name='get_auth_token')
]
