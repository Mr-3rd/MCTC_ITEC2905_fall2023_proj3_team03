"""
This API call will return the 5 highest rated autoshops that are near the users current location

geocoder reference: https://stackoverflow.com/questions/24906833/how-to-access-current-location-of-any-user-using-python

"""

import requests
from pprint import pprint #
import geocoder
import logging
import os

def get_location():
    g = geocoder.ip('me')
    return g.latlng

get_location()

def get_shops():
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
    'limit':5
    }

    businesses = []
    

    try:
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        data = response.json()

        for business in data['businesses']:

            name = business['name']
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


    except requests.HTTPError as HTerror: 
        logging.exception(HTerror)
        print('An HTTP error has occurred.')
        return HTerror 

    except requests.exceptions.Timeout: 
        error = 'Request has timed out' 
        logging.exception(error)
        print('The request has timed out.')
        return error

    except requests.exceptions.RequestException: 
        error = 'Error occurred while processing request' 
        logging.exception(error) 
        print('An error has occurred while processing this request' )
        return error


shops = get_shops()

for shop in shops:
    pprint(shop)