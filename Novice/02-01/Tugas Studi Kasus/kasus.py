Mahasiswa = {
    'nama' : 'Nita Rosiana',
    'nim' : 1700016085,
    'prodi' : 'Sistem Informasi',
    'fakultas' : 'FAST'
}
nama = Mahasiswa.get('nama')
print("Nama     : ", nama)
nim = Mahasiswa.get('nim')
print("Nim      : ", nim)
prodi = Mahasiswa.get('prodi')
print("Prodi    : ", prodi)
fakultas = Mahasiswa.get('fakultas')
print("Fakultas : ", fakultas)

def nilai_hasil(nil_presensi, nil_harian, nil_kuis, nil_uts, nil_uas):
    nil_presensi = int(nil_presensi) * 0.05
    nil_harian = int(nil_harian) * 0.15
    nil_kuis = int(nil_kuis) * 0.2
    nil_uts = int(nil_uts) * 0.3
    nil_uas = int(nil_uas) * 0.3

    nil_total = nil_presensi + nil_harian + nil_kuis + nil_uts + nil_uas
    return nil_total

def nilai_huruf(var_nilai):
    var_huruf = ""
    if (var_nilai >= 0 and var_nilai < 20):
        var_huruf = "E"
    elif (var_nilai >= 20 and var_nilai < 40):
        var_huruf = "D"
    elif (var_nilai >= 40 and var_nilai < 60):
        var_huruf = "C"
    elif (var_nilai  >=60 and var_nilai < 80):
        var_huruf = "B"
    elif (var_nilai >=80 and var_nilai <= 100):
        var_huruf = "A"

    return var_huruf

def hasil():
    nil_hasil_total = 0
    print("=======Nilai Akhir Semester=======")
    nil_presensi = input("Nilai Presensi : ")
    nil_harian = input("Nilai Harian   : ")
    nil_kuis = input("Nilai Kuis     : ")
    nil_uts = input("Nilai Uts      : ")
    nil_uas = input("Nilai Uas      : ")
        
    nil_hasil_total += (int(nilai_hasil(nil_presensi, nil_harian, nil_kuis, nil_uts, nil_uas)))
        
    return nil_hasil_total 

nil_total = hasil()

print("===========Total Nilai============")
print("Total nilai yang didapat: ",nil_total)

print("Nilai dalam Huruf       : ", nilai_huruf(nil_total))