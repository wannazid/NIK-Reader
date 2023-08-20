# NIK Reader
Sebuah library untuk membaca data dari kode NIK pada E-KTP. Yang akan menghasilkan seperti tempat lahir, tanggal lahir, gender, nomor pendaftaran.
# Install module
```
pip install git+https://github.com/wannazid/NIK-Reader
```
## Import module
```PYTHON
import nikreader
```
## Akses database
```PYTHON
db = nikreader.Database()
```
## Kode NIK
```PYTHON
nik = 'kode-nik'
```
### Cek provinsi, kabupaten dan kecamatan
```PYTHON
prov = db.cek_provonsi(nik)
kab = db.cek_kota(nik)
kec = db.cek_kecamatan(nik)
```
### Cek gender
```PYTHON
gender = db.cek_gender(nik)
```
### Cek tanggal lahir
```PYTHON
tanggal= db.cek_tanggal_lahir(nik)
bulan = db.cek_bulan_lahir(nik)
tahun = db.cek_tahun_lahir(nik)
```
### Cek nomor pendaftaran
```PYTHON
daftar = db.cek_daftar(nik)
```
### Contoh code
```PYTHON
import nikreader

db = nikreader.Database()
nik = 'kode-nik'

print(db.cek_provinsi(nik))
print(db.cek_kota(nik))
print(db.cek_kecamatan(nik))
print(db.cek_gender(nik))
print(db.cek_tanggal_lahir(nik))
print(db.cek_bulan_lahir(nik))
print(db.cek_tahun_lahir(nik))
print(db.cek_daftar(nik))
```
# Penutup
Sebenernya sudah banyak yang membuat nik reader seperti ini namun saya mencoba membuatnya dengan bahasa python karena kebanyakan membuatnya dari bahasa php, javascript dll. Semoga suka dengan module nya hehe. Terima Kasih sudah menggunakan:)


