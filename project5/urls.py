"""
URL configuration for project5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('school_form_cbv',school_form_cbv.as_view(),name="school_form_cbv"),
    path('school_list_cbv',school_list_cbv.as_view(),name="school_list_cbv"),
    path('school_list',school_list.as_view(),name="school_list"),
    path('school_insert',school_insert.as_view(),name="school_insert"),
    path('update/<pk>',school_update.as_view(),name="school_update"),
    path('details/<pk>',displayschool.as_view(),name="displayschool")
]
