from bangunruang import BangunRuang

class Bola(BangunRuang):
    def __init__(self):
        super().__init__()
        self.jari_jari = 0

    def volume_bola(self):
        self.panjang = self.jari_jari
        return super().volume_bola()

# br = Bola()
# br.jari_jari = 3
# hasil = br.volume_bola()
# print(hasil)