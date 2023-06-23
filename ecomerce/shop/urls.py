"""
URL configuration for ecomerce project.

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
from django.urls import path,include
from shop import views
app_name='shop'

urlpatterns = [
    path('',views.allprodcat,name='allprodcat'),
    path('allproducts/<slug:cslug>',views.allproducts,name='allproducts'),
    path('prodetails/<slug:pslug>', views.prodetails, name='prodetails'),
    path('reg', views.reg, name='reg'),
    path('log', views.user_login, name='log'),
    path('logo', views.user_logout, name='logo'),

]
