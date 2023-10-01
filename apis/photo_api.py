"""
Tesint API code for Flickr, to be imported into API server
"""
import requests

def get_car_images(color, year, make, model):
    search = color + '  "' + year + ' ' + make + ' ' + model +'"'
    api_key = '69d2a5d3d8d58ff369379c070f274857'
    method = 'flickr.photos.search'
    sort = 'relevance'
    safe_search = 1
    per_page = 5
    page = 1

    url = 'https://www.flickr.com/services/rest/'

    payload = { 'api_key': api_key, 'method': method, 'safe_search': safe_search, 'text':search, 'per_page':per_page, 'page':page, 'sort':sort}

    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        data = response.xml()
        return data, None
    except Exception as e:
        print(e)
        print(response.text)
        return None, e
        

color = 'Red'
year = '2012'
make = 'Fiat'
model = '500'

# color = 'Silver'
# year = '2017'
# make = 'Toyota'
# model = 'Camry'

get_car_images(color, year, make, model)