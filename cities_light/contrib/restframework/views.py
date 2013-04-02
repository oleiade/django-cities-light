# -*- coding: utf-8 -*-

# Copyright (c) 2013 theo crevon
#
# See the file LICENSE for copying permission.


from rest_framework import generics

from cities_light.models import City, Region, Country

from .filters import CityFilter, RegionFilter, CountryFilter
from .serializers import CitySerializer, RegionSerializer,\
                         CountrySerializer


class CityList(generics.ListAPIView):
    """API endpoint listing cities"""
    model = City
    serializer_class = CitySerializer
    filter_class = CityFilter


class CityDetail(generics.RetrieveAPIView):
    """API endpoint retrieving a single city"""
    model = City
    serializer_class = CitySerializer


class RegionList(generics.ListAPIView):
    """API endpoint listing regions"""
    model = Region
    serializer_class = RegionSerializer
    filter_class = RegionFilter


class RegionDetail(generics.RetrieveAPIView):
    """API endpoint retrieving a single region"""
    model = Region
    serializer_class = RegionSerializer


class CountryList(generics.ListAPIView):
    """API endpoint listing countries"""
    model = Country
    serializer_class = CountrySerializer
    filter_class = CountryFilter


class CountryDetail(generics.RetrieveAPIView):
    """API endpoint retrieving a single country"""
    model = Country
    serializer_class = CountrySerializer