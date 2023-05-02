from django.urls import path
from .views import api_countries, api_country, api_cities, api_city

urlpatterns = [
    path("country/", api_countries, name="api_countries"),
    path("country/<int:id>/", api_country, name="api_country"),
    path("city/", api_cities, name="api_cities"),
    path("city/<int:id>/", api_city, name="api_city"),
]
