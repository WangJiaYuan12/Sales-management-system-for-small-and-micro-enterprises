"""businesses URL Configuration

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
from django.urls import path, include
from Ftapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', views.index, name='index'),
    path('order/', views.Showorder, name='order'),
    path('salesman/', views.Showsalesman, name='salesman'),
    path('supplier/', views.Showsupplier, name='supplier'),
    path('gooods/', views.Showgoods, name='goods'),
    path('logo/', views.denglu, name='logo'),
    path('register/', views.zhuce, name='register'),
    path('captcha/', include('captcha.urls')),
    path('logout/',views.logout,name='logout'),
    path('amend/<int:us1>',views.ShowAmend,name='amend'),
    path('orderDetail/<int:order_id>',views.ShoworderDetail,name='orderDetail'),
    path('goodsDetail/<int:goods_id>', views.ShowgoodsDetail, name='goodsDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
