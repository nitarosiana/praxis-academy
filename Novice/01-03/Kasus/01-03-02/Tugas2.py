import datetime
import time

waktu = time.time()
sekarang = datetime.today()
tanggal = sekarang.date()

print ('Hari = ',tanggal.day)
print ('Bulan = ',tanggal.month)
print ('Tahun = ',tanggal.year)
print ('jam = ',waktu.hour)
print ('Menit = ',waktu.minute)
print ('Detik = ',waktu.second)
