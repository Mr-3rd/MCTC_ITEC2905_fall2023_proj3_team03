"""
This API call will return the 5 highest rated autoshops that are near the users current location
The geocoder library gets the latitude and longitude of the current user.
The API takes in a car object then uses the API to search for auto repair shops. 
The response then extracts the name, URL, rating, street address, city, state and then will create a dictionary with these values.
If there are any errors, it catches and logs the error, then returns an error message.

geocoder reference: https://stackoverflow.com/questions/24906833/how-to-access-current-location-of-any-user-using-python

logging reference: https://docs.python.org/3/library/logging.html#levels

"""

import requests
import geocoder
import logging
import os

# gets lat/long of user's current location using geocoder library
def get_location():
    g = geocoder.ip('me')
    return g.latlng

def get_shops(year, make, model):

    car = {'year': year, 'make': make, 'model': model }

    # API call
    url = "https://api.yelp.com/v3/businesses/search?"
    # gets API key from os
    API_key = os.environ.get('YELP_API_KEY')
    # calls the get_location function, gets users lat/long
    location = get_location()

    # authorizes the API key
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer " + API_key
    }

    # query parameters
    payload = {
    'latitude': location[0],
    'longitude': location[1],
    'categories': 'autorepair',
    'sort_by': 'rating', 
    'limit':5,
    'term': car['make']
    }

    # initializes and empty list to store API reuest results
    businesses = []
    

    try:
        # collects the data response from Yelp
        response = requests.get(url, headers=headers, params=payload)
        # checks if there's an error in the response
        response.raise_for_status()
        # retrieves the JSON data from response
        data = response.json()

        # iterates over businesses
        for business in data['businesses']:

            # extracts name, URL, rating, street address, city, and state
            # dictionary is created with these values
            business = {
            'name': business['name'],
            'url': business['url'],
            'rating':  business['rating'],
            'street_address': business['location']['address1'],
            'city': business['location']['city'],
            'state': business['location']['state']

            }
            businesses.append(business)
        # list is returned in a dictionary
        return businesses


    # error handling - HTTP error, a timeout error, or any other exception
    # logs error and returns an error message
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