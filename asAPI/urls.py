"""asAPI URL Configuration

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

from asAPI.views import return_asInfo_With_AS_Number, return_asInfo_With_IP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asinfowithasnum/<int:as_number>/', return_asInfo_With_AS_Number , name='return_asInfo_With_AS_Number'),
    # Create a new URL for the function return_asInfo_With_IP with a regexp for the ip_address:
    path('asinfowithip/<int:ip_address1>.<int:ip_address2>.<int:ip_address3>.<int:ip_address4>/', return_asInfo_With_IP , name='return_asInfo_With_IP'),
]
