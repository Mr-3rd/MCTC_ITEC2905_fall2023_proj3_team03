"""
This API call will return the 5 highest rated autoshops that are near the users current location

geocoder reference: https://stackoverflow.com/questions/24906833/how-to-access-current-location-of-any-user-using-python

"""

import requests
import geocoder
import logging
import os

def get_location():
    g = geocoder.ip('me')
    return g.latlng

get_location()

def get_shops(car):
    url = "https://api.yelp.com/v3/businesses/search?"
    API_key = os.environ.get('YELP_API_KEY')
    location = get_location()

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_key
    }

    payload = {
    'latitude': location[0],
    'longitude': location[1],
    'categories': 'autorepair',
    'sort_by': 'rating', 
    'limit':5,
    'term': car['make']
    }

    businesses = []
    

    try:
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        data = response.json()

        for business in data['businesses']:

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


    except requests.HTTPError as HTerror: 
        logging.exception(HTerror)
        error = 'Website error: ' + str(response.status_code)
        return error
    except requests.exceptions.Timeout: 
        error = 'The website has timed out' 
        logging.exception(error)
        return error
    except Exception:
        error = 'A catastrophic error has occurred: '
        logging.exception(error)
        return error