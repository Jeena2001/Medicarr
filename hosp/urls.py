"""hosp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from hospapp.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index,name='index'),
    url(r'^index',index,name='index'),
      url(r'^patienthome',patienthome,name='patienthome'),
    url(r'^doctors',doctors,name='doctors'),
    url(r'^login',login,name='login'),
    url(r'^logaction/$',logaction,name='logaction'),
     url(r'^patient',patient,name='patient'),
     url(r'^dele/',dele,name='dele'),
      url(r'^pre/',pre,name='pre'),
      url(r'^viewpre/',viewpre,name='viewpre'),
       url(r'^preaction/',preaction,name='preaction'),
     url(r'^viewpat',viewpat,name='viewpat'),
     url(r'^paction/$',paction,name='paction'),
     url(r'^pdaction/$',pdaction,name='pdaction'),
       url(r'^update/',update,name='update'),
        url(r'^logout/$',logout,name='logout'),
         url(r'^addp/$',addp,name='addp'),
           url(r'^detailaction/',detailaction,name='detailaction'),
]
