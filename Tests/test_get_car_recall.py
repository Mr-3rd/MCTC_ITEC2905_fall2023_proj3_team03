'''
Test get_car_recall

'''
import unittest
from unittest import TestCase

import sys
sys.path.append('..')
from apis import car_recall_api


class GetCarRecallTest(TestCase):

    def test_three_inputs(self): 
        expected = (None, 
        {'count': 4, 
         'results': [
        {'ReportReceivedDate': '15/11/2019', 'Component': 'Power Train:Automatic Transmission:Lever And Linkage:Floor Shift', 'Summary': 'Chrysler (fca us llc) is recalling certain 2012-2013 fiat 500 vehicles equipped with 6-speed automatic transmissions.  the shifter cable bushing may fail allowing the cable to detach from the transmission.'}, 
        {'ReportReceivedDate': '03/07/2019', 'Component': 'Power Train:Manual Transmission:Floor Shift Assembly', 'Summary': 'Dlt, llc. is recalling certain cravenspeed fiat short shifter shafts sold for use in 2011-2019 fiat 500 vehicles.  the shifter shaft may have been improperly manufactured with a through hole for the set screw rather than a blind hole, which may lead to the breakage of the shifter shaft.'}, 
        {'ReportReceivedDate': '16/05/2016', 'Component': 'Power Train:Manual Transmission', 'Summary': 'Chrysler (fca us llc) is recalling certain model year 2012-2016 fiat 500 vehicles manufactured june 21, 2010, through january 12, 2016, equipped with a manual transmission.  the clutch diaphragm spring may fracture and fail, causing an inability to switch gears.'}, {'ReportReceivedDate': '10/11/2011', 'Component': 'Service Brakes, Hydraulic:Fluid', 'Summary': 'Chrysler is recalling certain model year 2012 dodge journey and fiat 500 vehicles manufactured from october 24, 2011, through october 26, 2011.  some vehicles were assembled with contaminated brake fluid and may experience a degradation of the sealing components within the brake system.'}]})
        
        self.assertEqual(expected, car_recall_api.get_car_recall(2012, 'fiat', '500'))

    def test_one_empty_input(self):
        expected = ('No recalls Found for this vehicle', None)
        self.assertEqual(expected, car_recall_api.get_car_recall('', 'fiat', '500'))

    def test_two_empty_inputs(self):
        expected = ('No recalls Found for this vehicle', None)
        self.assertEqual(expected, car_recall_api.get_car_recall('', '', '500'))
    
    def test_three_empty_inputs(self):
        expected = ('No recalls Found for this vehicle', None)
        self.assertEqual(expected, car_recall_api.get_car_recall('', '', ''))

    def test_three_spaces_as_inputs(self):
        expected = ('No recalls Found for this vehicle', None)
        self.assertEqual(expected, car_recall_api.get_car_recall(' ', ' ', ' '))
        
    # def test_no_internet_connection(self):
    #     expected = ('A catastrophic error has occurred', None)
    #     self.assertEqual(expected, car_recall_api.get_car_recall(2012, 'fiat', '500'))
    

if __name__ == '__main__':
    unittest.main()