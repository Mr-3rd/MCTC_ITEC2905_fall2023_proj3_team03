"""
This API service takes in a car object, in the form of dictionary to make an
API call to Flickr that returns a list of 3 car photo titles and photo links for a specific Year Make and Model.
In the event of an error the details are logged to the system, and a user message string is returned

XML reference: https://www.tutorialspoint.com/python/python_xml_processing.htm

XML Parser and error handling reference: https://stackoverflow.com/questions/47917787/xml-etree-elementtree-parseerror-exception-handling-not-catching-errors

XML documentation Source: https://docs.python.org/3/library/xml.etree.elementtree.html

XML Root and findall usage: https://www.geeksforgeeks.org/xml-parsing-python/

"""
import requests
import xml.etree.ElementTree as ET
import logging
import os


def get_car_images(year, make, model):
    # turn the input into a dictionary
    car = {'year': year, 'make': make, 'model': model }

    # Create a blank list to hold the title and photo link of each image
    photo_links = []
    # Concatenate the car object with strings form a tailored search criteria, this avoids racecars and nascars
    search = '"' + car['year'] + ' ' + car['make'] + ' ' + car['model'] + '" car, -Stock -Race'
    # Collect the api key from the system
    api_key = os.environ.get('FLICKR_API')
    # select the method to request from the REST services flickr server
    method = 'flickr.photos.search'
    #find the most relevant photos
    sort = 'relevance'
    # On
    safe_search = 1
    per_page = 3
    page = 1
    # Size w is 400 PX picture size
    size = '_w'
    # photos only
    content_types = 0

    # create the api call URL and query parameters for the search
    url = 'https://www.flickr.com/services/rest/'
    payload = { 'api_key': api_key, 'method': method, 'safe_search': safe_search, 'text':search,
                'per_page':per_page, 'page':page, 'sort':sort, 'content_types':content_types}

    try:
        # collect the XML data response from Flickr
        response = requests.get(url, params=payload)
        # raise a status to create an error if not found, server error and other type of server error
        response.raise_for_status()

        # todo: make a parser for error handling
        # 
        # create an XML element structure from the response data 
        data = ET.fromstring(response.content)

        # Loop over each photo element and append the title and required photo server elements as a link in a object 
        for element in data.findall('.//photo'):
            photo_links.append({'title': element.get('title'), 'link': "https://live.staticflickr.com/" + element.get('server') + '/' + element.get('id') + '_' + element.get('secret') + size + ".jpg"})

        # if there are no photos returned in the list return a string with  that message
        if len(photo_links) == 0:
            error = 'No photos found for this vehicle'
            return error
        else:
            return photo_links

    # error handling block for call returns an error message as a string and logs the error to the system
    except requests.HTTPError as HTerror:
        error = 'An error has occurred: ' + str(response.status_code)
        logging.exception(HTerror)
        return error
    except requests.exceptions.Timeout:
        error = 'The website has timed out'
        logging.exception(error)
        return error
    except Exception:
        error = 'A catastrophic error has occurred'
        logging.exception(error)
        return error
        