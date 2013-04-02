# Django rest framework integration

django-cities-light `restframework` package let's you easily bind
django cities light models to `django-rest-framework` endpoints easily.

This `README` assumes you're already familiar with a django application setup, 
and with django-rest-framework usage more specifically.


### Important notice

* This `contrib` package is only compatible with `django-rest-framework` >= 2.0
* It relies on the `django-filter` package (used to provide generic 
`restframework` urls filters)


### Usage

First, you have to make sur `django-filter` is installed:

```shell
pip install django-filter
```

And, that you've also set the filter backend to `DjangoFilterBackend` in your `restframework` project settings:

```python
REST_FRAMEWORK = {
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend'
}
```


Then, all is left to do is adding `cities_light.contrib.restframework.urls` modules to your project urls:

```python
    url(r'^api/',
        include('cities_light.contrib.restframework.urls')),
```

**Nota**

`cities_light.contrib.restframework` exposes a urlpatterns variable like a classic django application, with the following urls:

* `cities_light_api_city_list`
* `cities_light_api_city_detail`
* `cities_light_api_region_list`
* `cities_light_api_region_detail`
* `cities_light_api_country_list`
* `cities_light_api_country_detail`





If djangorestframework is installed, all you have to do is add this url
include::



And that's all !