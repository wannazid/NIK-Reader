# contoh penggunaan module nikreader

# import module nikreader
import nikreader

# membuka database
db = nikreader.Database()

# kode nik (str)
nik = '3401070505050001'

# cek provinsi nik
provinsi = db.cek_provinsi(nik)
# cek kabupaten nik
kab = db.cek_kota(nik)
# cek kecamatan nik
kec = db.cek_kecamatan(nik)
# cek gender nik
gender = db.cek_gender(nik)
# cek tanggal lahir nik
tgl = db.cek_tanggal_lahir(nik)
#cek bulan lahir nik
bln = db.cek_bulan_lahir(nik)
# cek tahun lahir nik 
thn = db.cek_tahun_lahir(nik)
# cek nomor pendaftaran di hari yang sama
daftar = db.cek_daftar(nik)


print(provinsi)
print(kab)
print(kec)
print(gender)
print(tgl)
print(bln)
print(thn)
print(daftar)