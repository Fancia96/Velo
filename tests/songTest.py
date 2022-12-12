import unittest
from hamcrest import *

from classes.song import return_verse


class SongTest(unittest.TestCase):

    def test_empty_strands(self):
        vers_1 = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
        self.assertEqual(return_verse(1), vers_1)
