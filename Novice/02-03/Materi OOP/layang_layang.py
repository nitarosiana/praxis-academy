from bangundatar import BangunDatar

# penurunan sifat inheritance
class Layang_layang(BangunDatar):
    #overide
    def __init__(self):
        super().__init__()
        self.diagonal1 = 0
        self.diagonal2 = 0

    #overide
    def luas_layang_layang(self):
        self.panjang = self.diagonal1
        self.lebar = self.diagonal2
        return super().luas_layang_layang()

#bd = Layang_layang()
#bd.diagonal1 = 30
#bd.diagonal2 = 15
#hasil = bd.luas_layang_layang()
#print(hasil)