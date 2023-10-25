""""

shops_api testing

"""
import unittest
from unittest import TestCase

import sys
sys.path.append('..')
from apis import shops_api

class GetShopsTest(TestCase):

    def test_three_car_params(self):
        expected = (None,
 [{'city': 'Minneapolis',
   'name': 'FIAT of Minneapolis',
   'rating': 4.0,
   'state': 'MN',
   'street_address': '1820 Quentin Ave',
   'url': 'https://www.yelp.com/biz/fiat-of-minneapolis-minneapolis-4?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
     {'city': 'Hopkins',
   'name': 'Luther Hopkins Honda',
   'rating': 3.5,
   'state': 'MN',
   'street_address': '250 5th Ave S',
   'url': 'https://www.yelp.com/biz/luther-hopkins-honda-hopkins-2?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'St Louis Park',
   'name': 'Alfa Romeo of Minneapolis',
   'rating': 3.5,
   'state': 'MN',
   'street_address': '1820 Quentin Ave',
   'url': 'https://www.yelp.com/biz/alfa-romeo-of-minneapolis-st-louis-park-2?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'Minneapolis',
   'name': 'Top Gear Autoworks',
   'rating': 2.5,
   'state': 'MN',
   'street_address': '3412 Cedar Ave S',
   'url': 'https://www.yelp.com/biz/top-gear-autoworks-minneapolis?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'Saint Louis Park',
   'name': 'Luther Westside Volkswagen',
   'rating': 2.5,
   'state': 'MN',
   'street_address': '2370 Hwy 100 S',
   'url': 'https://www.yelp.com/biz/luther-westside-volkswagen-saint-louis-park?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'}])
        self.assertEqual(expected, shops_api.get_shops(2012, 'Fiat', '500'))


    def test_invalid_year(self):
        expected = (None,
 [{'city': 'Edina',
   'name': 'Samaritan Tire Pros',
   'rating': 5.0,
   'state': 'MN',
   'street_address': '3224 Southdale Circle Dr',
   'url': 'https://www.yelp.com/biz/samaritan-tire-pros-edina?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'Lakeville',
   'name': "LaMettry's Collision, Inc.",
   'rating': 5.0,
   'state': 'MN',
   'street_address': '21023 Cedar Ave',
   'url': 'https://www.yelp.com/biz/lamettrys-collision-inc-lakeville-4?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'Golden Valley',
   'name': 'Poquet Auto Sales',
   'rating': 5.0,
   'state': 'MN',
   'street_address': '800 Lilac Dr N',
   'url': 'https://www.yelp.com/biz/poquet-auto-sales-golden-valley-2?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'San Mateo',
   'name': 'Di Auto Specialist',
   'rating': 5.0,
   'state': 'CA',
   'street_address': None,
   'url': 'https://www.yelp.com/biz/di-auto-specialist-san-mateo-3?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'},
  {'city': 'Eden Prairie',
   'name': "Leighton's Garage",
      'rating': 5.0,
   'state': 'MN',
   'street_address': '14301 W 62nd St',
   'url': 'https://www.yelp.com/biz/leightons-garage-eden-prairie?adjust_creative=wnNPSzlPAupEVUrA6kEVTg&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=wnNPSzlPAupEVUrA6kEVTg'}])
        self.assertEqual(expected, shops_api.get_shops(439257439573409, 'porsche', '911'))

    def test_invalid_make_model(self):
        expected = ('No businesses found for this vehicle', None)
        self.assertEqual(expected, shops_api.get_shops(2012, 'bcjsbjbdvbv', '119'))


# TODO Add unit tests for if the user runs out of API calls

# TODO Add mock unit tests

if __name__ == '__main__':
    unittest.main()