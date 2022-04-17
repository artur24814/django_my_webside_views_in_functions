"""testowa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from moja_strona import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('work/', views.work, name='list_product'),
    path('opinion/', views.opinion),
    path('order/', views.order),
    path('product_info/<int:id_product>/', views.product_info, name='result'),
    path('your_order/<str:email>/', views.your_order),
    path('delete_order/<int:id>/', views.delete_order),
    path('create_opinion/', views.create_opinion)
]
