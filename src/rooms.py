from src.guests import Guests
from src.songs import Songs


class Rooms:

    def __init__(self, people, till, genre, fee):
        self.people = people
        self.till = till
        self.genre = genre 
        self.fee = fee



    
    def check_in(self):
        people = self.people + 1
        return people

    def check_out(self):
        people = self.people - 1
        return people

    def max_capacity(self):
        if self.people > 9:
            self.check_out
            return "Room is full"

        

    # def fav_song(self, guests):
    #     if fav_song == self.guests2.fav_song:
    #         return print("Whooo i love this song!!!")
    #     else fav_song != self.guests2.fav_song:
    #         return print("I hate this song")

