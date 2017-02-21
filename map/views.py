from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .utils.geoPic import geoPic
from rest_framework import viewsets
from .serializers import PlaceSerializer

def mapindex(request):
    return render(request, 'mapindex.html')


def mapupload(request):
    if request.method == 'POST':
        imgs = request.FILES.getlist('img')
        for img in imgs:
            info = geoPic(img)
            if info is None:
                print(img, 'has no geo info')
                continue
            p = Place()
            p.img = img
            p.date, p.time, p.lat, p.lng = info
            p.save()
        return HttpResponse(u'image upload success <a href="../">查看地图</a>')
    return render(request, 'mapupload.html')

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
