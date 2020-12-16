from bangundatar import BangunDatar

# penurunan sifat inheritance
class Persegi(BangunDatar):
    #overide
    def __init__(self):
        super().__init__()
        self.sisi = 0

    #overide
    def hitung_luas(self):
        self.panjang = self.sisi
        self.lebar = self.sisi
        return super().hitung_luas()

    def keliling_persegi(self):
        self.panjang = self.sisi
        return super().keliling_persegi()

        
# kotak = Persegi()
# kotak.sisi = 5
# hasil = kotak.hitung_luas()
# print(hasil)

# kotak = Persegi()
# kotak.sisi = 5
# hasil = kotak.keliling_persegi()
# print(hasil)
