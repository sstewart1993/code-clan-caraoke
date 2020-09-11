import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    def setUp(self):
        self.songs = Songs("Highway to Hell", "ACDC", "rock")


    def test_song_title(self):
        title = self.songs.name
        self.assertEqual("Highway to Hell", title)

    def test_song_artist(self):
        artist = self.songs.artist
        self.assertEqual("ACDC", artist)

    def test_genre(self):
        genre = self.songs.genre
        self.assertEqual("rock", genre)