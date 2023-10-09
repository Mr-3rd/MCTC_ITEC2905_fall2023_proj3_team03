""""


"""

import shops_api

car = {'year': '2012', 'make': 'Fiat', 'model': '500'}


def display_shops(car):
    shops = shops_api.get_shops(car)

    if type(shops) == str:
        print(shops)
    else:
        for shop in shops:
            print(shop)

car = {'year': '2012', 'make': 'Fiat', 'model': '500'}
display_shops(car)

car = {'year': '', 'make': '', 'model': ''}
display_shops(car)

car = {'year': '2021', 'make': 'porsche', 'model': '911'}
display_shops(car)

