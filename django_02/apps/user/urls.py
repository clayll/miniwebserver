"""fresh_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import re_path
from apps.user import views

urlpatterns = [
    # url(r'user/register_user$', views.register_user),
    re_path(r'^register$', views.Register_view.as_view(), name='register'),
    re_path(r'^active/(?P<id>.*)$', views.Active_view.as_view(), name='active'),
    re_path(r'^login', views.Login_view.as_view(), name='login'),
    re_path(r'^logout', views.Logout_View.as_view(), name='logout'),
    re_path(r"^user", views.UserInfo_View.as_view(), name='user'),
    re_path(r"^order", views.UserOrder_View.as_view(), name='order'),
    re_path(r"^address", views.Address_View.as_view(), name='address')
]
