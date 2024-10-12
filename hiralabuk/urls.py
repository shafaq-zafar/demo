"""
URL configuration for hiralabuk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('Contactus', views.Contactus, name='Contactus'),
    path('saveforms', views.saveforms, name='saveforms'),
    path('gallery', views.gallery),
    path('Download', views.Download),
    path('Accreditations', views.Accreditations),
    path('Digital', views.Digital),
    path('test', views.test),
    path('home', views.home),
    path('Scanbody', views.Scanbody),
    path('Scan', views.Scan),
    path('Specialize', views.Specialize),
    path('aboutus', views.aboutus),
    path('how1', views.how1, name='how1'),
    path('how2', views.how2, name='how2'),
    path('how3', views.how3, name='how3'),
    path('how4', views.how4, name='how4'),
    path('how5', views.how5, name='how5'),
    path('how6', views.how6, name='how6'),
    path('clear', views.clear, name='clear'),
    path('crown', views.crown, name='crown'),
    path('dental', views.dental, name='dental'),
    path('fully', views.fully, name='fully'),
    path('pressure', views.pressure, name='pressure'),
]
