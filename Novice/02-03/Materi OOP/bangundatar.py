from kalkulator import Kalkulator

class BangunDatar:
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0
        self.alat_hitung = Kalkulator()
    def hitung_luas(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        return self.alat_hitung.perkalian()
    
    def keliling_persegi(self):
        self.alat_hitung.a = self.panjang
        return self.alat_hitung.a * 4

    def luas_segitiga(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        return self.alat_hitung.perkalian() / 2

    def luas_trapesium(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        self.alat_hitung.c = self.tinggi
        return self.alat_hitung.penjumlahan() * self.tinggi / 2
    
    def luas_lingkaran(self):
        self.alat_hitung.a = self.panjang
        phi = 3.14
        return self.alat_hitung.pangkat() * phi

    def luas_layang_layang(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        return self.alat_hitung.perkalian() / 2



#triplek = BangunDatar()
#triplek.a = 3
#triplek.b = 2
#print(triplek.hitung_luas())