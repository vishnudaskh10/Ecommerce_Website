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
from django.urls import path
from django.urls import path,include
from cart import views
app_name='cart'

urlpatterns = [
    path('addcart/<int:p>',views.Addcart,name='Addcart'),
    path('cart_view',views.cart_view,name='cart_view'),
    path('decreaser/<int:p>/',views.decreaser,name='decreaser'),
    path('dele/<int:p>',views.dele,name='dele'),
    path('accnt/',views.accnt,name='accnt'),
    path('order/',views.orderview1,name='orderview1'),
]

