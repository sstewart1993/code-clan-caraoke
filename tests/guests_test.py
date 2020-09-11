import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestGuests(unittest.TestCase):
    
    def setUp(self):
        self.guests = Guests("Steve", 50.00, "Highway to Hell")
        self.rooms = Rooms(6, 24.40, "Rock")
        self.songs = Songs("Highway to Hell", "ACDC", "rock")

    def test_name(self):
        name = self.guests.name
        self.assertEqual("Steve", name)

    def test_wallet(self):
        wallet = self.guests.wallet
        self.assertEqual(50.00, wallet)

    def test_fav_song(self):
        fav_song = self.guests.fav_song
        self.assertEqual("Highway to Hell", fav_song)
    
