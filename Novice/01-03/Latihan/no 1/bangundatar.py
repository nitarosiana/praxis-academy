class BangunDatar:
    def __init__(self):
        self.panjang = 0
        self.lebar = 0

    def hitung_luas(self):
        return self.panjang * self.lebar

triplek = BangunDatar()
#triplek.a = 3
#triplek.b = 2

print(triplek.hitung_luas())