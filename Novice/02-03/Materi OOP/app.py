from kubus import Kubus
from tabung import Tabung
from kerucut import Kerucut
from bola import Bola
from limas_segiempat import Limas_Segiempat

# kotak = Kubus()
# kotak.sisi = 5
# hasil = kotak.volume_kubus()
# print(hasil)

# kotak = Kubus()
# kotak.sisi = 5
# hasil = kotak.luas_permukaan_kubus()
# print(hasil)

# br = Tabung()
# br.jari_jari = 5
# br.tinggi = 12
# hasil = br.volume_tabung()
# print(hasil)

# br = Kerucut()
# br.jari_jari = 5
# br.tinggi = 12
# hasil = br.volume_kerucut()
# print(hasil)

# br = Bola()
# br.jari_jari = 3
# hasil = br.volume_bola()
# print(hasil)

br = Limas_Segiempat()
br.panjang = 6
br.lebar = 3
br.tinggi = 8
hasil = br.volume_limas_segiempat()
print(hasil)