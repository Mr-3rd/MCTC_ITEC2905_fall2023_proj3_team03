"""
This API function call will connect to the NHTSA API and return up to 4 recalls that a 
car has.

"""

import requests

def get_car_recall(year, make, model):
    recall_results = []
    nhtsa_url = 'https://api.nhtsa.gov/recalls/recallsByVehicle'

    if make == '' or model == '' or year == '':
            raise ValueError('Sorry, you must enter a value.')
    nhtsa_query = {'make': make, 'model': model, 'modelYear': year, 'timeout': 30}

    try: 
        nhtsa_response = requests.get(nhtsa_url , params=nhtsa_query)
        nhtsa_response.raise_for_status() # raise exception for 400 or 500 errors
        nhtsa_data = nhtsa_response.json()

        count = nhtsa_data['Count']

        for recall in nhtsa_data['results']:
            recall_results.append({'ReportReceivedDate': recall['ReportReceivedDate'], 'Component': recall['Component'].title(),
                                   'Summary': recall['Summary'].capitalize()})
        return count, recall_results
        
    except Exception as ex: #todo: make more explicit error handling
        print('Sorry, unable to search car.', ex)

