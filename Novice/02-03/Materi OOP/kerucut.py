from bangunruang import BangunRuang

class Kerucut(BangunRuang):
    def __init__(self):
        super().__init__()
        self.jari_jari = 0
        self.tinggi = 0

    def volume_kerucut(self):
        self.panjang = self.jari_jari
        self.tinggi = self.tinggi
        return super().volume_kerucut()

# br = Kerucut()
# br.jari_jari = 5
# br.tinggi = 12
# hasil = br.volume_kerucut()
# print(hasil)