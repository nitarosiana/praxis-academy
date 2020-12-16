from bangunruang import BangunRuang

class Limas_Segiempat(BangunRuang):
    def __init__(self):
        super().__init__()
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0

    def volume_limas_segiempat(self):
        self.panjang = self.panjang
        self.lebar = self.lebar
        self.tinggi = self.tinggi
        return super().volume_limas_segiempat()

# br = Limas_Segiempat()
# br.panjang = 6
# br.lebar = 3
# br.tinggi = 8
# hasil = br.volume_limas_segiempat()
# print(hasil)