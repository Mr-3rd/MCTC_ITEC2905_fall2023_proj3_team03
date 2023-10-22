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
          logging.info(f'About to make request to Recall API at url {nhtsa_url} with PAYLOAD: {nhtsa_query}')

          nhtsa_response = requests.get(nhtsa_url , params=nhtsa_query)

          # nhtsa_response.raise_for_status() # raise exception for 400 or 500 errors

          logging.debug(f'response received from API {nhtsa_response}, PAYLOAD: {nhtsa_query}')
          nhtsa_data = nhtsa_response.json()

          logging.debug(f'data received from API {nhtsa_data}, CONTENT: {nhtsa_response.content}')

          recall_results['count'] = nhtsa_data['Count']

          logging.info(f'Recalls Found: {nhtsa_data["Count"]}')

          recall_results['results'] = [] # blank list will store only the needed data from the nhtsa recall in dictionary objects

          # nhtsa data is sorted by date in descending order, this will improve user experience when data is displayed
          sorted_recalls = sorted(nhtsa_data['results'], key=lambda x: datetime.strptime(x['ReportReceivedDate'], '%d/%m/%Y'), reverse=True)

          for recall in sorted_recalls: # append ReportReceivedDate, Component and Summary data from nhtsa api call data
               recall_results['results'].append({'ReportReceivedDate': recall['ReportReceivedDate'], 'Component': recall['Component'].title(),
                                   'Summary': recall['Summary'].capitalize()})

          if len(sorted_recalls) != 0:
               return None, recall_results
          else:
               error = "No recalls Found for this vehicle"
               return error, None
    
    # error handling block for call returns an error message as a string and logs the error to the system
    except requests.HTTPError as HTerror:
         error = 'An error has occurred: ' + str(nhtsa_response.status_code)
         logging.exception(HTerror)
         return error, None
    except requests.exceptions.Timeout:
         error = 'The website has timed out'
         logging.exception(error)
         return error, None
    except Exception:
         error = 'A catastrophic error has occurred'
         logging.exception(error)
         return error, None