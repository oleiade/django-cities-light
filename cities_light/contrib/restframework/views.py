from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from cities_light.models import City, Region, Country
from .serializers import CitySerializer, RegionSerializer,\
	CountrySerializer


class CityList(generics.ListAPIView):
	"""API endpoint listing cities"""
	model = City
	serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
	"""API endpoint retrieving a single city"""
	model = City
	serializer_class = CitySerializer


class RegionList(generics.ListAPIView):
	"""API endpoint listing regions"""
	model = Region
	serializer_class = RegionSerializer


class RegionDetail(generics.RetrieveAPIView):
	"""API endpoint retrieving a single region"""
	model = Region
	serializer_class = RegionSerializer


class CountryList(generics.ListAPIView):
	"""API endpoint listing countries"""
	model = Country
	serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveAPIView):
	"""API endpoint retrieving a single country"""
	model = Country
	serializer_class = CountrySerializer