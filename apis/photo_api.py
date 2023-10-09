"""
Test API code for Flickr, to be imported into API server

XML reference: https://www.tutorialspoint.com/python/python_xml_processing.htm


"""
import requests
import xml.etree.ElementTree as ET
import os

def get_car_images(car):

    photo_links = []

    search = '"' + car['year'] + ' ' + car['make'] + ' ' + car['model'] + '" car, -Stock -Race'
    api_key = os.environ.get('FLICKR_API')
    print(api_key)
    method = 'flickr.photos.search'
    sort = 'relevance'
    safe_search = 1
    per_page = 3
    page = 1
    size = '_w'  # blank is 500 PX
    content_types = 0

    url = 'https://www.flickr.com/services/rest/'

    payload = { 'api_key': api_key, 'method': method, 'safe_search': safe_search, 'text':search,
                'per_page':per_page, 'page':page, 'sort':sort, 'content_types':content_types}

    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()

        data = ET.fromstring(response.content)

        for element in data.findall('.//photo'):
            photo_links.append({'title': element.get('title'), 'link': "https://live.staticflickr.com/" + element.get('server') + '/' + element.get('id') + '_' + element.get('secret') + size + ".jpg"})

        if len(photo_links) == 0:
            error = 'No photos found for this vehicle'
            return error
        else:
            return photo_links

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
        