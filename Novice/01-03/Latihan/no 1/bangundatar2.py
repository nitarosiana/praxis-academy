from Kalkulator import Kalkulator

class BangunDatar:
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.alat_hitung = Kalkulator()

    def hitung_luas(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        return self.alat_hitung.perkalian()

triplek = BangunDatar()
triplek.a = 3
triplek.b = 2
print(triplek.hitung_luas())