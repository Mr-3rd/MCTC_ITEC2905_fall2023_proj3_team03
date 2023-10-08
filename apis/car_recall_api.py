"""
This API function call will connect to the NHTSA API and return up to 4 recalls that a 
car has.

"""

import requests
from functools import cache
from datetime import datetime


@cache
def get_car_recall(year, make, model):
    recall_results = {}

    nhtsa_url = 'https://api.nhtsa.gov/recalls/recallsByVehicle'

    if make == '' or model == '' or year == '':
            raise ValueError('Sorry, you must enter a value.')
    nhtsa_query = {'make': make, 'model': model, 'modelYear': year, 'timeout': 30}

    try: 
        nhtsa_response = requests.get(nhtsa_url , params=nhtsa_query)
        nhtsa_response.raise_for_status() # raise exception for 400 or 500 errors
        nhtsa_data = nhtsa_response.json()

        recall_results['Count'] = nhtsa_data['Count']

        recall_results['results'] = []

        sorted_recalls = sorted(nhtsa_data['results'], key=lambda x: datetime.strptime(x['ReportReceivedDate'], '%d/%m/%Y'))

        for recall in sorted_recalls:
            recall_results['results'].append({'ReportReceivedDate': recall['ReportReceivedDate'], 'Component': recall['Component'].title(),
                                   'Summary': recall['Summary'].capitalize()})

        return recall_results
    
    # explicit error handling
    except requests.exceptions.InvalidSchema as schema_er: 
        print('Sorry, unable to search car. InvalidSchema Error:', schema_er)

    except requests.exceptions.ConnectionError as conn_er: 
        print('Sorry, unable to search car. Connecion Error:', conn_er)

    except requests.exceptions.HTTPError as http_er: 
        print('Sorry, unable to search car. HTTP Error:', http_er)
    
    except requests.exceptions.RequestException as req_er:
         print('Sorry, unable to search car. Error:', req_er)

    except Exception as er:
         print('Sorry, unable to search car.', er)    

get_car_recall(2012, 'fiat', '500')
