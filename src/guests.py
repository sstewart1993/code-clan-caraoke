class Guests:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def afford_entry(self, rooms, guests):
        if guests.wallet >= rooms.fee:
            guests.wallet -= rooms.fee
            return print("Welcome, have a good time.")
        else:
            guests.wallet < rooms.fee
            return print("Not tonight pal.")
