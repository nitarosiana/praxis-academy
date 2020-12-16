from persegi import Persegi
from segitiga import Segitiga
from trapesium import Trapesium
from lingkaran import Lingkaran
from layang_layang import Layang_layang

#kotak = Persegi()
#kotak.sisi = 5
#hasil = kotak.hitung_luas()
#print(hasil)

# kotak = Persegi()
# kotak.sisi = 5
# hasil = kotak.keliling_persegi()
# print(hasil)

#bd = Segitiga()
#bd.alas = 5
#bd.tinggi = 4
#hasil = bd.luas_segitiga()
#print(hasil)

#bd= Trapesium()
#bd.atas = 8
#bd.bawah = 12
#bd.tinggi = 6
#hasil = bd.luas_trapesium()
#print(hasil)

#b = Lingkaran()
#bd.jari_jari = 5
#hasil = bd.luas_lingkaran()
#print(hasil)

bd = Layang_layang()
bd.diagonal1 = 30
bd.diagonal2 = 15
hasil = bd.luas_layang_layang()
print(hasil)