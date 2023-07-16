"""
URL configuration for University project.

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
from university.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/anzahl/aktiveStudenten',show_aktive_studenten_anzahl),
    path('service/anzahl/Professoren',show_dozenten_anzahl),
    path('professoren',show_professoren_all),
    path('professoren/json',show_professoren_all_json),
    path('x/service/anzahl/aktiveStudenten',x_show_aktive_studenten_anzahl,name='x_service_anzahl_aktiveStudenten'),
    path('x/professoren',x_show_professoren_all,name='x_show_prof'),
    path('x/professoren/json',x_show_professoren_all_json),
    path('',show_index),
]


