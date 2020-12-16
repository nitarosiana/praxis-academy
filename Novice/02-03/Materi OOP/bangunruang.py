from kalkulator import Kalkulator

class BangunRuang:
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0
        self.alat_hitung = Kalkulator()
    def volume_kubus(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        self.alat_hitung.c = self.tinggi
        return self.alat_hitung.perkalian() * self.tinggi

    def luas_permukaan_kubus(self):
        self.alat_hitung.a = self.panjang
        return self.alat_hitung.pangkat() * 6

    def volume_tabung(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.c = self.tinggi
        phi = 3.14
        return self.alat_hitung.pangkat() * phi * self.tinggi

    def volume_kerucut(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.c = self.tinggi
        phi = 3.14
        return self.alat_hitung.pangkat() * phi * self.tinggi / 3

    def volume_bola(self):
        self.alat_hitung.a = self.panjang
        phi = 3.14
        return self.alat_hitung.kubik() * phi * 4/3

    def volume_limas_segiempat(self):
        self.alat_hitung.a = self.panjang
        self.alat_hitung.b = self.lebar
        self.alat_hitung.c = self.tinggi
        return self.alat_hitung.perkalian() * self.tinggi * 1/3