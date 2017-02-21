"""Travelling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from map.views import mapindex
from map.views import mapupload
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from map.views import PlaceViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', mapupload, name = 'upload'),
    url(r'^$', mapindex),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
