'''
Test recall videos

'''
import unittest
from unittest import TestCase

import sys
sys.path.append('..')
from apis import video_api


class GetCarRecallTest(TestCase):

    def test_valid_12_Fiat_500(self): 
        expected = (None, [{'title': 'Easy Transmission Shift Cable Bushing Replacement: HOW TO ESCAPE', 'embed': 'https://www.youtube.com/embed/G4V32X0XSxU'}, 
                           {'title': 'Fiat 500 manual transmission clutch lockout switch replacement, repair starting issues', 
                            'embed': 'https://www.youtube.com/embed/a7RfhDbWYyI'},
                              {'title': 'Fiat 500 owners complain about dangerous clutch problems',
                             'embed': 'https://www.youtube.com/embed/S_AXrs179Lc'},
                               {'title': 'SYMPTOMS OF A BAD BRAKE MASTER CYLINDER', 'embed': 'https://www.youtube.com/embed/8eL1FZf5Oes'}])
        
        self.assertEqual(expected, video_api.get_car_videos('2012', 'fiat', '500'))

    def test_empty_input(self):
        expected = ('Car recall videos not found', None)
        self.assertEqual(expected, video_api.get_car_videos('', '', ''))

    def test_crazy_car(self):
        year = '1900'
        make = 'Tilken'
        model = 'Mustoong'

        expected = ('No photos found for this vehicle', None)
        self.assertEqual(expected, video_api.get_car_videos(year, make, model))





if __name__ == '__main__':
    unittest.main()
