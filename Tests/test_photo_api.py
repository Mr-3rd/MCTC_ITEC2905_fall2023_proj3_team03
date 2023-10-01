"""

"""

import photo_api

def display_car(car):
    for photo in car:
        print(photo['title'])
        print(photo['link'])

color = 'Red'
year = '2012'
make = 'Fiat'
model = '500'

fiat = photo_api.get_car_images(color, year, make, model)

display_car(fiat)

color = 'Silver'
year = '2017'
make = 'Toyota'
model = 'Camry'

camry = photo_api.get_car_images(color, year, make, model)

display_car(camry)

color = 'green'
year = '1965'
make = 'Ford'
model = 'Mustang'

mustang = photo_api.get_car_images(color, year, make, model)

display_car(mustang)