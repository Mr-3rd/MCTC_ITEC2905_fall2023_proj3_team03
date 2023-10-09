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

car = {'year': year, 'make': make, 'model': model}

fiat = photo_api.get_car_images(car)
print(fiat)

display_car(fiat)

color = ''
year = '2017'
make = 'Toyota'
model = 'Camry'

car = {'year': year, 'make': make, 'model': model}

camry = photo_api.get_car_images(car)
print(camry)


display_car(camry)

color = ''
year = '1965'
make = 'Ford'
model = 'Mustang'

car = {'year': year, 'make': make, 'model': model}

mustang = photo_api.get_car_images(car)

print(mustang)

display_car(mustang)

color = ''
year = '1900'
make = 'Tilken'
model = 'Mustoong'

car = {'year': year, 'make': make, 'model': model}

mustoong = photo_api.get_car_images(car)

print(mustoong)

display_car(mustoong)