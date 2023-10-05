"""

"""

import requests
from pprint import pprint #
import geocoder
import logging

def get_location():
    g = geocoder.ip('me')
    return g.latlng

get_location()

def get_shops():
    url = "https://api.yelp.com/v3/businesses/search?"

    location = get_location()

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer Mffa79XK8JY420sd-OXXHCk-N_wPQ_vwfjsCrFO0PVZ3nXljHNP5ZCali_I5Shv9JZdDd53dxrXdxFWjwT7azo0caDOV1VFc8KF4qK_ljAAYXa6VpHvobMOgXmYXZXYx"
    }

    payload = {
    'latitude': location[0],
    'longitude': location[1],
    'categories': 'autorepair',
    'sort_by': 'rating', 
    'limit':5

    }


    businesses = []
    

    try:
        response = requests.get(url, headers=headers, params=payload)
        data = response.json()

        # pprint(data)
        for business in data['businesses']:

            name = business['name']
            # print(business['image_url'])
            url = business['url']
            rating = business['rating']
            street_address = business['location']['address1']
            city = business['location']['city']
            state = business['location']['state']

            business = {
            'name': business['name'],
            'url': business['url'],
            'rating':  business['rating'],
            'street_address': business['location']['address1'],
            'city': business['location']['city'],
            'state': business['location']['state']

            }
            businesses.append(business)
        return businesses



    # add dictionary to get sorted list

    except requests.HTTPError as HTerror: 

        logging.exception(HTerror)

        return HTerror 

    except requests.exceptions.Timeout: 
        error = 'Catastrophic error occurred' 
        logging.exception(error)

        return  error

    except requests.exceptions.RequestException: 
        error = 'Catastrophic error occurred' 
        logging.exception(error) 
        return  error


# get_shops()
# location = get_location
# print(location)
shops = get_shops()

for shop in shops:
    print(shop)