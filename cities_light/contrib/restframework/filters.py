import django_filters

from cities_light.models import City, Region, Country


class CityFilter(django_filters.FilterSet):
    search_names = django_filters.CharFilter(lookup_type='icontains')
    
    class Meta:
        model = City
        fields = ['country', 'region', 'search_names']


class RegionFilter(django_filters.FilterSet):
	# support a `icontains` based ?search_name param which
	# filters results based on region ascii name
	search_name = django_filters.CharFilter(name='name_ascii', lookup_type='icontains')

	class Meta:
		model = Region
		fields = ['country', 'search_name']


class CountryFilter(django_filters.FilterSet):
	search_name = django_filters.CharFilter(name='name_ascii', lookup_type='icontains')

	class Meta:
		model = Country
		fields = ['search_name']