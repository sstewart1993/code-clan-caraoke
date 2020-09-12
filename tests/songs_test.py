import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs1 = Songs("Highway to Hell", "ACDC", "rock")
        self.songs2 = Songs("Sk8er Boi", "Avril Lavigne", "pop")
        self.songs3 = Songs("9 to 5", "Dolly Parton", "country")


    def test_song_title(self):
        title = self.songs1.name
        self.assertEqual("Highway to Hell", title)

    def test_song_artist(self):
        artist = self.songs2.artist
        self.assertEqual("Avril Lavigne", artist)

    def test_genre(self):
        genre = self.songs3.genre
        self.assertEqual("country", genre)