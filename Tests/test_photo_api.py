'''
Test car photos

'''
import unittest
from unittest import TestCase

import sys
sys.path.append('..')
from apis import photo_api


class GetCarRecallTest(TestCase):

    def test_valid_12_Fiat_500(self): 
        expected = (None, [{'title': '2012 Fiat 500 Abarth', 
                            'link': 'https://live.staticflickr.com/7207/6838497826_533da1c937_w.jpg'}, 
                            {'title': '2012 Fiat 500', 
                             'link': 'https://live.staticflickr.com/5084/5215566906_3860b05920_w.jpg'}, 
                             {'title': '2012 Fiat 500 CCW LM16', 
                              'link': 'https://live.staticflickr.com/8290/7746429344_57cb10aaba_w.jpg'}])
        
        self.assertEqual(expected, photo_api.get_car_images('2012', 'fiat', '500'))

    def test_empty_input(self):
        expected = ('No photos found for this vehicle', None)
        self.assertEqual(expected, photo_api.get_car_images('', '', ''))



if __name__ == '__main__':
    unittest.main()