"""balancing URL Configuration

The `urlpatterns` list routes URLs to folder_of_views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function folder_of_views
    1. Add an import:  from my_app import folder_of_views
    2. Add a URL to urlpatterns:  path('', folder_of_views.home, name='home')
Class-based folder_of_views
    1. Add an import:  from other_app.folder_of_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kpibalancing/', include('balancingapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
