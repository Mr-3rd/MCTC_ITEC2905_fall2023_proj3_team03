"""
This API function call will connect to the NHTSA API and return up to 4 recalls that a 
car has.

"""

import requests
from functools import cache
from datetime import datetime
import logging

@cache
def get_car_recall(year, make, model):
    
    car = {'year': year, 'make': make, 'model': model }

    recall_results = {'count': 0, 'results' : ''}

    nhtsa_url = 'https://api.nhtsa.gov/recalls/recallsByVehicle'
    nhtsa_query = {'make': car['make'], 'model': car['model'], 'modelYear': car['year'], 'timeout': 30}

    try: 
        nhtsa_response = requests.get(nhtsa_url , params=nhtsa_query)
        nhtsa_response.raise_for_status() # raise exception for 400 or 500 errors
        nhtsa_data = nhtsa_response.json()

        recall_results['Count'] = nhtsa_data['Count']

        recall_results['results'] = []

        sorted_recalls = sorted(nhtsa_data['results'], key=lambda x: datetime.strptime(x['ReportReceivedDate'], '%d/%m/%Y'), reverse=True)

        for recall in sorted_recalls:
            recall_results['results'].append({'ReportReceivedDate': recall['ReportReceivedDate'], 'Component': recall['Component'].title(),
                                   'Summary': recall['Summary'].capitalize()})

        return recall_results
    
    # explict error handling
    except requests.HTTPError as HTerror:
         error = 'An error has occurred: ' + str(nhtsa_response.status_code)
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

