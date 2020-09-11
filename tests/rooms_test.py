import unittest
from src.rooms import Rooms

class TestRooms(unittest.TestCase):
    def setUp(self):
        self.rooms = Rooms(6, 24.40, "Rock")

    def test_how_many_in_the_room(self):
        no_of_people = self.rooms.people
        self.assertEqual(6, no_of_people)

    def test_till(self):
        till = self.rooms.till
        self.assertEqual(24.40, till)
    
    def test_type_of_music(self):
        genre = self.rooms.genre
        self.assertEqual("Rock", genre)
    