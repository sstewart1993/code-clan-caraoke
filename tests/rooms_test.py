import unittest
from src.rooms import Rooms
from src.guests import Guests

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.rooms1 = Rooms(6, 24.40, "Rock")
        self.rooms2 = Rooms(10, 32.0, "Pop")
        self.rooms3 = Rooms(2, 12.20, "Country")

    def test_how_many_in_the_room(self):
        no_of_people = self.rooms1.people
        self.assertEqual(6, no_of_people)

    def test_till(self):
        till = self.rooms1.till
        self.assertEqual(24.40, till)
    
    def test_type_of_music(self):
        genre = self.rooms1.genre
        self.assertEqual("Rock", genre)

    def test_check_in(self):
        how_many_in_the_room = self.rooms1.people + 1
        self.assertEqual(7, how_many_in_the_room)

    def test_check_out(self):
        how_many_in_the_room = self.rooms1.people - 1
        self.assertEqual(5, how_many_in_the_room)

    def test_max_capacity(self):
        how_many_in_the_room = self.rooms2.people
        if how_many_in_the_room > 9:
            return print("Room is full")

    def test_fav_song(self):
        self.rooms.fav_song(guests)
        self.guests2.fav_song 
        self.assertEqual()

        


    