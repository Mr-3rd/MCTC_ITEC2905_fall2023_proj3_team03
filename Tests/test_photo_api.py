"""

"""

import photo_api

def display_car(car):

    if type(car) == str:
        print(car)
    elif type(car) == list:
        for photo in car:
            print(photo['title'])
            print(photo['link'])        
    else:
        print('serious error occurred')

color = ''
year = '2012'
make = 'Fiat'
model = '500'

fiat = photo_api.get_car_images(color, year, make, model)
print(fiat)

display_car(fiat)

color = ''
year = '2017'
make = 'Toyota'
model = 'Camry'

camry = photo_api.get_car_images(color, year, make, model)
print(camry)


display_car(camry)

color = ''
year = '1965'
make = 'Ford'
model = 'Mustang'

mustang = photo_api.get_car_images(color, year, make, model)

print(mustang)

display_car(mustang)

color = ''
year = '1900'
make = 'Tilken'
model = 'Mustoong'

mustoong = photo_api.get_car_images(color, year, make, model)

print(mustoong)

display_car(mustoong)