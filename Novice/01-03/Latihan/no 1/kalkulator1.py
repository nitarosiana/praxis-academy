
class Kalkulator:
    #methods
    def penjumlahan(self):
        return self.a + self.b

    def pengurang(self):
        return self.a - self.b

    def perkalian(self):
        return self.a * self.b

    def pembagian(self):
        return self.a / self.b

casio = Kalkulator()

casio.a = 2
casio.b = 3

hasil = casio.penjumlahan()
print(hasil)