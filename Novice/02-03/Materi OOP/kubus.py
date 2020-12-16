from bangunruang import BangunRuang

class Kubus(BangunRuang):
    def __init__(self):
        super().__init__()
        self.sisi = 0

    def volume_kubus(self):
        self.panjang = self.sisi
        self.lebar = self.sisi
        self.tinggi = self.sisi
        return super().volume_kubus()

    def luas_permukaan_kubus(self):
        self.panjang = self.sisi
        return super().luas_permukaan_kubus()

# kotak = Kubus()
# kotak.sisi = 5
# hasil = kotak.volume_kubus()
# print(hasil)

# kotak = Kubus()
# kotak.sisi = 5
# hasil = kotak.luas_permukaan_kubus()
# print(hasil)