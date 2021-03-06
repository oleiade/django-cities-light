# -*- coding: utf-8 -*-

# Copyright (c) 2013 theo crevon
#
# See the file LICENSE for copying permission.

from django.conf.urls.defaults import patterns, url

from .views import CityList, CityDetail, RegionList,\
                   RegionDetail, CountryList, CountryDetail

urlpatterns = patterns('',
    url(r'^cities/$',
        CityList.as_view(),
        name='cities_light_api_city_list',
    ),

    url(r'^cities/(?P<pk>[^/]+)/$',
        CityDetail.as_view(),
        name='cities_light_api_city_detail',
    ),

    url(r'^regions/$',
        RegionList.as_view(),
        name='cities_light_api_region_list',
    ),

    url(r'^regions/(?P<pk>[^/]+)/$',
        RegionDetail.as_view(),
        name='cities_light_api_region_detail',
    ),

    url(r'^countries/$',
        CountryList.as_view(),
        name='cities_light_api_country_list',
    ),

    url(r'^countries/(?P<pk>[^/]+)/$',
        CountryDetail.as_view(),
        name='cities_light_api_country_detail',
    ),
)