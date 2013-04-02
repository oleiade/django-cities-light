from django.conf.urls.defaults import patterns, url
from django.core import urlresolvers

from .views import CityList, CityDetail, RegionList,\
                   RegionDetail, CountryList, CountryDetail

urlpatterns = patterns('',
    url(r'^city/$',
        CityList.as_view(),
        name='cities_light_api_city_list',
    ),

    url(r'^city/(?P<pk>[^/]+)/$',
        CityDetail.as_view(),
        name='cities_light_api_city_detail',
    ),

    url(r'^region/$',
        RegionList.as_view(),
        name='cities_light_api_region_list',
    ),

    url(r'^region/(?P<pk>[^/]+)/$',
        RegionDetail.as_view(),
        name='cities_light_api_region_detail',
    ),

    url(r'^country/$',
        CountryList.as_view(),
        name='cities_light_api_country_list',
    ),

    url(r'^country/(?P<pk>[^/]+)/$',
        CountryDetail.as_view(),
        name='cities_light_api_country_detail',
    ),
)