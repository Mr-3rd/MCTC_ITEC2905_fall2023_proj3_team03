"""
Test API code for YouTube, to be imported into API server

XML reference: https://www.tutorialspoint.com/python/python_xml_processing.htm


"""
import requests
import os
import logging


def get_car_videos(car , recalls):

    video_links = []

    search_url = 'https://www.googleapis.com/youtube/v3/search'

    # search_url = 'https://www.googleapis.com/youtube/v3/'

    api_key = os.environ.get('YOUTUBE_API')

    query = '' + car['year'] + ' ' + car['make'] + ' ' + car['model'] + ', '

    for recall in recalls['recalls']:

        new_query = query + recall['Component'].lower().replace(':', ' ') +' recall'

        payload = {
            'key': api_key,
            'q' : new_query,
            'part' : 'snippet',
            'maxResults' : 1,
            'type' : 'video'
        }

        try:
            response = requests.get(search_url, params=payload)
            response.raise_for_status()

            data = response.json()['items']

            for element in data:

                title = element['snippet']['title']
                embed = 'https://www.youtube.com/embed/' + element['id']['videoId']

                video_links.append({'title': title, 'embed': embed})

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
        

    if len(video_links) == 0:
        return 'Car recall videos not found'
    else:
        return video_links
    