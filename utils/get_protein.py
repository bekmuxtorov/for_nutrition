import requests
import json


url = 'https://api.nal.usda.gov/fdc/v1/foods/search'


async def get_nutrients(fruit_name: str) -> dict:

    params = {
        'api_key': 'pDJwte1u9SKcwyQR3r84kWV1TzGqZXifbJMxmVgc',
        'query': f'{fruit_name}',
        'dataType': ["Survey (FNDDS)"],
        'pagesize': 5,
    }

    res = requests.get(url, params=params)
    response = json.loads(res.content)

    if len(response["foods"]) == 0:
        data = {"status": False}
        return data

    data = {
        "status": True,
        fruit_name: {
            "protein": response["foods"][0]["foodNutrients"][0],    # oqsil
            "lipid": response["foods"][0]["foodNutrients"][1],       # yog'
            "energy": response["foods"][0]["foodNutrients"][3],      # kaloriya
            "alcohol": response["foods"][0]["foodNutrients"][4],    # alkogol
            "caffeine": response["foods"][0]["foodNutrients"][6],    # kafein
            "sugar": response["foods"][0]["foodNutrients"][8],      # shakar
            "calcium": response["foods"][0]["foodNutrients"][10],    # kalsin
            "iron": response["foods"][0]["foodNutrients"][11],      # temir
            "magnesium": response["foods"][0]["foodNutrients"][12],    # magniy
            "phosphorus": response["foods"][0]["foodNutrients"][13],  # fosfor
            "potassium": response["foods"][0]["foodNutrients"][14],    # kaliy
        }
    }

    return data 
    