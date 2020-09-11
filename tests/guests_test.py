import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestGuests(unittest.TestCase):
    
    def setUp(self):
        self.guests1 = Guests("Steve", 50.00, "Highway to Hell")
        self.guests2 = Guests("Rob", 26.40, "Sk8er Boi")
        self.guests3 = Guests("Sally", 68.30, "9 to 5")

    def test_name(self):
        name = self.guests1.name
        self.assertEqual("Steve", name)

    def test_wallet(self):
        wallet = self.guests1.wallet
        self.assertEqual(50.00, wallet)

    def test_fav_song(self):
        fav_song = self.guests2.fav_song
        self.assertEqual("Sk8er Boi", fav_song)
    
