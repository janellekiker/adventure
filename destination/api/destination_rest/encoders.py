from common.json import ModelEncoder
from .models import Country, City

class CountryEncoder(ModelEncoder):
    model = Country
    properties = [
        "name",
        "continent",
        "id"
    ]


class CityEncoder(ModelEncoder):
    model = City
    properties = [
        "name",
        "country"
    ]
    encoders = {
        "country": CountryEncoder()
    }
