from bangundatar import BangunDatar

# penurunan sifat inheritance
class Lingkaran(BangunDatar):
    #overide
    def __init__(self):
        super().__init__()
        self.jari_jari = 0

    #overide
    def luas_lingkaran(self):
        self.panjang = self.jari_jari
        return super().luas_lingkaran() 

#bd = Lingkaran()
#bd.jari_jari = 5
#hasil = bd.luas_lingkaran()
#print(hasil)