
from os.path import join
import errno
import shutil
import unittest
from tempfile import mkdtemp, mkstemp

from landsat import utils

def test_geocode():
       loc = utils.geocode('Hawa Mahal, Jaipur, Rajasthan')
       print (loc)

       self.assertEqual(round(loc['lat'], 3), 38.898)
       self.assertEqual(round(loc['lon'], 3), -77.037)
       self.assertRaises(ValueError, utils.geocode, 'Pennsylvania Ave NW, Washington, DC')
       self.assertEqual({'lat': 38.8987709, 'lon': -77.0351295},
                        utils.geocode('Pennsylvania Ave NW, Washington, DC'))

test_geocode()
