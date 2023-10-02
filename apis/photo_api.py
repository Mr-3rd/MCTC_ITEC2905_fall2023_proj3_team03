"""
Test API code for Flickr, to be imported into API server

XML reference: https://www.tutorialspoint.com/python/python_xml_processing.htm


"""
import requests
import xml.etree.ElementTree as ET

def get_car_images(color, year, make, model):

    photo_links = []

    search = color + ' "' + year + ' ' + make + ' ' + model + '" car, -Stock -Race'
    api_key = '69d2a5d3d8d58ff369379c070f274857'
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
            return 'Car is not found'
        else:
            return photo_links

    except Exception as e:
        print('An error has occurred: ')
        print(e)
        print(response.text)
        return e
        