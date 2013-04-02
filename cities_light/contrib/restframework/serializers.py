from rest_framework import serializers

from cities_light.models import City, Region, Country


class CitySerializer(serializers.ModelSerializer):
    """City model serializer"""
    # Hyperlinked relation to city's region
    region = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='cities_light_api_region_detail'
    )
    # Hyperlinked relation to city's country
    country = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='cities_light_api_country_detail'
    )

    class Meta:
        model = City


class RegionSerializer(serializers.ModelSerializer):
    """Region model serializer"""
    # Hyperlinked relation to region's country
    country = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='cities_light_api_country_detail'
    )

    class Meta:
        model = Region


class CountrySerializer(serializers.ModelSerializer):
    """Country model serializer"""
    class Meta:
        model = Country