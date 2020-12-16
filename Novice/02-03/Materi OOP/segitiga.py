from bangundatar import BangunDatar

# penurunan sifat inheritance
class Segitiga(BangunDatar):
    #overide
    def __init__(self):
        super().__init__()
        self.alas = 0
        self.tinggi = 0

    #overide
    def luas_segitiga(self):
        self.panjang = self.alas
        self.lebar = self.tinggi 
        return super().luas_segitiga() 

#bd = Segitiga()
#bd.alas = 5
#bd.tinggi = 4
#hasil = bd.luas_segitiga()
#print(hasil)