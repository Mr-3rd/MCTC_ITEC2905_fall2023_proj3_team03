"""
This API service takes in a car object and it's related recalls object in the form of dictionaries to make an
API call to youtube that returns a list of video titles and links for each of the recall components 
present for a specific Year Make and Model. In the event of an error the details are logged to the system, 
and a user message string is returned

YouTube Resource video: https://www.youtube.com/watch?v=jpessCuO4ug

Code in video: https://github.com/PrettyPrinted/youtube_video_code/tree/master/2019/07/28/Create%20a%20YouTube%20Search%20App%20in%20Flask%20Using%20the%20YouTube%20Data%20API

iFrame Embed API Reference: https://developers.google.com/youtube/iframe_api_reference

"""
import requests
import os
import logging


def get_car_videos(year, make, model , recalls):

    car = {'year': year, 'make': make, 'model': model }

    # initiate a blank list to hold the video elements
    video_links = []
    # create the list searching url that returns a set of video details from youtube
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    # collect the users api key from the environment
    api_key = os.environ.get('YOUTUBE_API')
    # create the search query used to locate videos, remove the year for potentially more accurate searches
    query = '' + car['year'] + ' ' + car['make'] + ' ' + car['model'] + ' '
    # loop over each recall in the list of recalls
    for recall in recalls['results']:
        # create a new query concatenating the car query with the lower case component
        new_query = query + recall['Component'].lower().replace(':', ' ') +' recall'
        # create the search payload and parameters with the new search
        payload = {
            'key': api_key,
            'q' : new_query,
            # snippet returns a portion of details from youtube, allows for simple public video id retention
            'part' : 'snippet',
            # 1 video per result, default search is relevance 
            'maxResults' : 1,
            # only videos
            'type' : 'video'
        }

        try:
            # collect the data response from YouTube with the payload
            response = requests.get(search_url, params=payload)
            # raise a status to create an error if not found, server error and other type of server error
            response.raise_for_status()

            # Create a json object referring to the items present in the snippet returned
            data = response.json()['items']

            # For each video in the data
            for element in data:
                # get the video title
                title = element['snippet']['title']
                # get the embedded video link
                embed = 'https://www.youtube.com/embed/' + element['id']['videoId']
                # append both to the list
                video_links.append({'title': title, 'embed': embed})

                # if there are no videos returned in the list return a string with  that message

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
        
    if len(video_links) == 0:
        return 'Car recall videos not found'
    else:
        return video_links
    