class Kalkulator:
    #methods
    def __init__(self):
        self.a = 0
        self.b = 0

    def penjumlahan(self):
        return self.a + self.b

    def pengurang(self):
        return self.a - self.b

    def perkalian(self):
        return self.a * self.b

    def pembagian(self):
        return self.a / self.b
        
    casio = Kalkulator()
    hasil = casio.penjumlahan()
    print("hasil default : ", hasil)
    
    casio.a = 2
    casio.b = 3
    hasil = casio.penjumlahan()
    print("hasil settingan : ", hasil)