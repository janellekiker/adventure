from django.http import JsonResponse
from .models import Country, City
from django.views.decorators.http import require_http_methods
import json
from .encoders import CountryEncoder, CityEncoder


# COUNTRY VIEW FUNCTIONS

@require_http_methods(["GET", "POST"])
def api_countries(request):
    # LIST ALL COUNTRIES
    if request.method == "GET":
        try:
            countries = Country.objects.all()
            return JsonResponse(
                countries,
                encoder=CountryEncoder,
                safe=False,
            )
        except:
            return JsonResponse(
                {"message": "Could not list countries"},
                status=400,
            )
    # CREATE NEW COUNTRY
    else: # POST
        try:
            content = json.loads(request.body)
            country = Country.objects.create(**content)
            return JsonResponse(
                country,
                encoder=CountryEncoder,
                safe=False,
            )
        except:
            return JsonResponse(
                {"message": "Could not create country"},
                status=400,
            )


@require_http_methods(["DELETE"])
def api_country(request, id):
    # DELETE A COUNTRY
    if request.method == "DELETE":
        try:
            country = Country.objects.get(id=id)
            country.delete()
            return JsonResponse(
                country,
                encoder=CountryEncoder,
                safe=False,
            )
        except Country.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# CITY VIEW FUNCTIONS

@require_http_methods(["GET", "POST"])
def api_cities(request):
    # LIST ALL CITIES
    if request.method == "GET":
        try:
            cities = City.objects.all()
            return JsonResponse(
                cities,
                encoder=CityEncoder,
                safe=False,
            )
        except:
            return JsonResponse(
                {"message": "Could not list cities"},
                status=400,
            )
    # CREATE NEW CITY
    else: # POST
        try:
            content = json.loads(request.body)
            # GET THE COUNTRY OBJECT AND PUT IT IN THE CONTENT DICT
            try:
                country_id = content["country"]
                country = Country.objects.get(id=country_id)
                content["country"] = country
            except Country.DoesNotExist:
                return JsonResponse(
                    {"message": "Invalid country id"},
                    status=404,
                )

            city = City.objects.create(**content)
            return JsonResponse(
                city,
                encoder=CityEncoder,
                safe=False,
            )
        except:
            return JsonResponse(
                {"message": "Could not create city"},
                status=400,
            )


@require_http_methods(["DELETE"])
def api_city(request, id):
    # DELETE A CITY
    if request.method == "DELETE":
        try:
            city = City.objects.get(id=id)
            city.delete()
            return JsonResponse(
                city,
                encoder=CityEncoder,
                safe=False,
            )
        except City.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )
