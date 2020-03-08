class mahasiswa():
    def __init__(self,nama,alamat,umur,jenis_kelamin):
        self.nama = nama
        self.alamat = alamat
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin
        print('(nama mahasiswa : {})'.format(self.nama))
    
    def tell(self):
        print('Nama: "{}" alamat:"{}"'.format(self.nama,self.alamat), end=" ")

class kampus(mahasiswa):
    def __init__(self,nama,alamat,no_telepon,kode_pos):
        mahasiswa.__init__(self,nama,alamat,no_telepon,kode_pos)
        self.no_telepon = no_telepon
        self.kode_pos = kode_pos
        print('(kuliah di : {})'.format(self.nama))
    
    def tell(self):
        mahasiswa.tell(self)
        print('no telepon : "{}"'.format(self.no_telepon))
        print('Kode pos : "{}"'.format(self.kode_pos))

mhs = mahasiswa('cinta','wonogiri',21,'P')
kmps = kampus('uad','jogja',12345,57662)

print()

total = [mhs,kmps]
for anggota in total:
    anggota.tell()
