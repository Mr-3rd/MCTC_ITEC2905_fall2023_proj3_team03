"""
Test API code for YouTube, to be imported into API server

XML reference: https://www.tutorialspoint.com/python/python_xml_processing.htm


"""
import requests
import xml.etree.ElementTree as ET
import os
from datetime import datetime

def get_car_videos(car , recalls):

    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    video_links = []

    search_url = 'https://www.googleapis.com/youtube/v3/search'

    api_key = os.environ.get('YOUTUBE_API')

    query = 'Recall:' + car['year'] + ' ' + car['make'] + ' ' + car['model'] + ' '

    for recall in recalls['recalls']:

        new_query = query + recall['Component'].lower().replace(':', ' ') + ' '

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

        except Exception as e:
            print('An error has occurred: ')
            print(e)
            print(response.text)
            return e
        

    if len(video_links) == 0:
        return 'Car recall videos not found'
    else:
        return video_links
    
car = {'year': '2012', 'make': 'Fiat', 'model': '500'}

recall_data = {'count': 4, 'recalls': [{'ReportReceivedDate': '10/11/2011', 'Component': 'Service Brakes, Hydraulic:Fluid', 'Summary': 'Chrysler is recalling certain model year 2012 dodge journey and fiat 500 vehicles manufactured from october 24, 2011, through october 26, 2011.  some vehicles were assembled with contaminated brake fluid and may experience a degradation of the sealing components within the brake system.'},
 {'ReportReceivedDate': '03/07/2019', 'Component': 'Power Train:Manual Transmission:Floor Shift Assembly', 'Summary': 'Dlt, llc. is recalling certain cravenspeed fiat short shifter shafts sold for use in 2011-2019 fiat 500 vehicles.  the shifter shaft may have been improperly manufactured with a through hole for the set screw rather than a blind hole, which may lead to the breakage of the shifter shaft.'},
 {'ReportReceivedDate': '16/05/2016', 'Component': 'Power Train:Manual Transmission', 'Summary': 'Chrysler (fca us llc) is recalling certain model year 2012-2016 fiat 500 vehicles manufactured june 21, 2010, through january 12, 2016, equipped with a manual transmission.  the clutch diaphragm spring may fracture and fail, causing an inability to switch gears.'},
 {'ReportReceivedDate': '15/11/2019', 'Component': 'Power Train:Automatic Transmission:Lever And Linkage:Floor Shift', 'Summary': 'Chrysler (fca us llc) is recalling certain 2012-2013 fiat 500 vehicles equipped with 6-speed automatic transmissions.  the shifter cable bushing may fail allowing the cable to detach from the transmission.'}] }

def display_recalls():
    print(recall_data['count'])
    recalls = recall_data['recalls']

    print(type(recalls))

    sorted_recalls = recalls.sort(key = lambda x: datetime.strptime(x['ReportReceivedDate'], '%d/%m/%Y'), reverse=True)

    print(sorted_recalls)

    for recall in recalls:
        print(recall['ReportReceivedDate'])
        print(recall['Component'])
        print(recall['Summary'] + '\n')

info = get_car_videos(car, recall_data)

print(info)