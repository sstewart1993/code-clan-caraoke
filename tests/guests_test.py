import unittest
from src.guests import Guests
from src.rooms import Rooms
from src.songs import Songs

class TestGuests(unittest.TestCase):
    
    def setUp(self):
        self.rooms1 = Rooms(6, 24.40, "Rock", 6.20)
        self.rooms2 = Rooms(10, 32.0, "Pop", 7.00)
        self.rooms3 = Rooms(2, 12.20, "Country", 2.50)

        self.guests1 = Guests("Steve", 50.00, "Highway to Hell")
        self.guests2 = Guests("Rob", 1.50, "Sk8er Boi")
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

    def test_afford_entry(self):
        self.guests1.afford_entry(self.rooms1, self.guests1)
        self.assertEqual(43.80, self.guests1.wallet)

    def test_cant_afford_entry(self):
        # poor_guest = Guests("John", 1.50, "Miami")
        self.guests2.afford_entry(self.rooms2, self.guests2)
        self.assertEqual(1.50, self.guests2.wallet)

        
    
