import django_filters

from cities_light.models import City, Region, Country


class CityFilter(django_filters.FilterSet):
    name_contains = django_filters.CharFilter(
    	name='search_names',
    	lookup_type='icontains'
    )
    name_startswith = django_filters.CharFilter(
    	name='search_names',
    	lookup_type='istartswith'
    )
    
    class Meta:
        model = City
        fields = [
        	'country',
        	'region',
        	'name_contains',
        	'name_startswith'
        ]


class RegionFilter(django_filters.FilterSet):
	# support a `icontains` based ?search_name param which
	# filters results based on region ascii name
	name_contains = django_filters.CharFilter(
		name='name_ascii', 
		lookup_type='icontains'
	)
	name_startswith = django_filters.CharFilter(
		name='name_ascii',
		lookup_type='istartswith'
	)

	class Meta:
		model = Region
		fields = [
			'country',
			'name_contains',
			'name_startswith'
		]


class CountryFilter(django_filters.FilterSet):
	name_contains = django_filters.CharFilter(
		name='name_ascii',
		lookup_type='icontains'
	)
	name_startswith = django_filters.CharFilter(
		name='name_ascii',
		lookup_type='istartswith'
	)
	class Meta:
		model = Country
		fields = [
			'name_contains',
			'name_startswith'
		]