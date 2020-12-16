from bangundatar import BangunDatar

# penurunan sifat inheritance
class Trapesium(BangunDatar):
    #overide
    def __init__(self):
        super().__init__()
        self.atas = 0
        self.bawah = 0
        self.tinggi = 0

    #overide
    def luas_trapesium(self):
        self.panjang = self.atas
        self.lebar = self.bawah
        self.tinggi = self.tinggi
        return super().luas_trapesium()

#bd= Trapesium()
#bd.atas = 8
#bd.bawah = 12
#bd.tinggi = 6
#hasil = bd.luas_trapesium()
#print(hasil)