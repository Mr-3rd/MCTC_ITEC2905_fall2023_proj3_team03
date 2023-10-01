"""
This API function call will connect to the NHTSA API and return up to 4 recalls that a 
car has.

"""

import requests

nhtsa_url = 'https://api.nhtsa.gov/recalls/recallsByVehicle'

def get_car_recall(make, model, year):

    try: 
        if make == '' or model == '' or year == '':
            raise ValueError('Sorry, you must enter a value.')
        nhtsa_query = {'make': make, 'model': model, 'modelYear': year,}

        nhtsa_response = requests.get(nhtsa_url , params=nhtsa_query)
        nhtsa_response.raise_for_status() # raise exception for 400 or 500 errors
        nhtsa_data = nhtsa_response.json()
        nhtsa_results = nhtsa_data['results']
        return nhtsa_results
        
    except Exception as ex:
        print('Sorry, unable to search car.', ex)

