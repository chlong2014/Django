""""
Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
"""""

from django.contrib import admin
from django.urls import path
from myapp01 import views as myviews #as 别名

urlpatterns = [
    path('admin/', admin.site.urls),
    #设置自己的URL
    path("test/", myviews.test),
    path("page/<str:pageName>", myviews.topage),
    #page/<str:pageName> restfulUrl<str:pageName>代表地址栏传递的参数
    #pageName要与视图函数的相同
    path("user/log/", myviews.login),
    path("user/reg/", myviews.reg),
]
