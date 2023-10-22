"""
This API call will return json data based on the year, make and model of a car.
The json data will include all documented recalls associated with the user's car of choice.


datetime reference for sorting: https://www.geeksforgeeks.org/python-sort-list-of-dates-given-as-strings/

"""

import requests
from functools import cache
from datetime import datetime
import logging

@cache
def get_car_recall(year, make, model):
    """This API service takes three parameters that is entered by a user using a form which makes 
    an API call to NHTSA that returns a json object based on the year, make and model of a car."""
    
    car = {'year': year, 'make': make, 'model': model }

    recall_results = {'count': '', 'results' : ''} 

    nhtsa_url = 'https://api.nhtsa.gov/recalls/recallsByVehicle'
    nhtsa_query = {'make': car['make'], 'model': car['model'], 'modelYear': car['year'], 'timeout': 30}

    try: 
        nhtsa_response = requests.get(nhtsa_url , params=nhtsa_query)
        nhtsa_response.raise_for_status() # raise exception for 400 or 500 errors
        nhtsa_data = nhtsa_response.json()

        recall_results['count'] = nhtsa_data['Count']

        recall_results['results'] = [] # blank list will store only the needed data from the nhtsa recall in dictionary objects

        sorted_recalls = sorted(nhtsa_data['results'], key=lambda x: datetime.strptime(x['ReportReceivedDate'], '%d/%m/%Y'), reverse=True)
        # nhtsa data is sorted by date in descending order, this will improve user experience when data is displayed

        for recall in sorted_recalls: # process ReportReceivedDate, Component and Summary data from nhtsa api call data
            recall_results['results'].append({'ReportReceivedDate': recall['ReportReceivedDate'], 'Component': recall['Component'].title(),
                                   'Summary': recall['Summary'].capitalize()})

        return recall_results
    
    # error handling block for call returns an error message as a string and logs the error to the system
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

