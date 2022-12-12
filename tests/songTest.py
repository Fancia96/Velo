import unittest
from hamcrest import *

from classes.song import return_verse


class SongTest(unittest.TestCase):

    def test_first_verse(self):
        vers_1 = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."
        self.assertEqual(return_verse(1), vers_1)

    def test_sixth_verse(self):
        vers_6 = "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(return_verse(6), vers_6)

    def test_eleventh_verse(self):
        vers_11 = "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
        self.assertEqual(return_verse(11), vers_11)
