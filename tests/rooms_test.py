import unittest
from src.rooms import Rooms
from src.guests import Guests
from src.songs import Songs

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.rooms1 = Rooms(6, 24.40, "Rock", 6.20)
        self.rooms2 = Rooms(10, 32.0, "Pop", 7.00)
        self.rooms3 = Rooms(2, 12.20, "Country", 2.50)

        self.songs1 = Songs("Highway to Hell", "ACDC", "rock")
        self.songs2 = Songs("Sk8er Boi", "Avril Lavigne", "pop")
        self.songs3 = Songs("9 to 5", "Dolly Parton", "country")

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
        how_many_in_the_room = self.rooms2.people - 1
        self.assertEqual(9, how_many_in_the_room)

    def test_max_capacity(self):
        how_many_in_the_room = self.rooms2.people
        if how_many_in_the_room >= 10:
            return print("Room is full")
    
    def test_fee(self):
        fee = self.rooms3.fee
        self.assertEqual(2.50, fee)

    # def test_add_song(self):
    #     new_song = self.rooms1.songs + self.songs1.name
    #     self.assertEqual("Highway to Hell", new_song)



    

        


    