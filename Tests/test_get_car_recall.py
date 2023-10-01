'''
Test get_car_recall

'''
import unittest
from unittest import TestCase

import sys
sys.path.append('..')
from apis.car_recall_api import get_car_recall


class GetCarRecallTest(TestCase):

    def test_three_inputs(self): 
        expected = get_car_recall('fiat', '500', 2012)
        self.assertEqual(expected, get_car_recall('fiat', '500', 2012))

        

