import geocoder
from .models import *
from django.shortcuts import render
from rest_framework.views import APIView
from main.serializers import *
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import generics


class ListCreatePizzerias(generics.ListCreateAPIView):
    queryset = Pizzerias.objects.all()
    serializer_class = PizzeriasSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('lat', 0)
        longitude = self.request.query_params.get('lng', 0)
        radius = self.request.query_params.get('rad', 0)

        if latitude and longitude:

            pnt = GEOSGeometry('POINT(' + str(latitude) + ' ' + str(longitude) + ')', srid=4326)

            for pizzarias in Pizzerias.objects.annotate(distance=Distance('coordinates', pnt)):
                diss = pizzarias.distance.km
                if float(radius) > float(diss):
                    list_pizz = list(Pizzerias.objects.annotate(distance=Distance(
                        'coordinates', pnt)).order_by('distance').order_by(
                        'distance').filter(distance__lte=float(radius)*1000))
                    return list_pizz