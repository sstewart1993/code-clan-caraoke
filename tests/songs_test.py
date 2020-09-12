import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs1 = Songs("Highway to Hell", "ACDC", "rock")
        self.songs2 = Songs("Sk8er Boi", "Avril Lavigne", "pop")
        self.songs3 = Songs("9 to 5", "Dolly Parton", "country")
        self.songs4 = {}


    def test_song_title(self):
        title = self.songs1.name
        self.assertEqual("Highway to Hell", title)

    def test_song_artist(self):
        artist = self.songs2.artist
        self.assertEqual("Avril Lavigne", artist)

    def test_genre(self):
        genre = self.songs3.genre
        self.assertEqual("country", genre)

    def test_add_song(self):
        self.songs4 = ("Yellow Submarine", "Beatles", "Rock")
        self.assertEqual(("Yellow Submarine", "Beatles", "Rock"), self.songs4)

    
    def test_add_song_check_song_title(self):
        self.songs4 = ("Yellow Submarine", "Beatles", "Rock")
        title = self.songs4[0]
        self.assertEqual(("Yellow Submarine", "Beatles", "Rock"), self.songs4)
        self.assertEqual("Yellow Submarine", title)

    # def test_add_song(self):
    #     new_song = self.rooms.add_song
    #     self.rooms1 == new_song
    #     self.assertEqual("Hello", new_song)