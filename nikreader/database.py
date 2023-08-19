import json
import os

class Database:
    def __init__(self, data_path=None):
        if data_path is None:
            nikreader_dir = os.path.dirname(os.path.abspath(__file__))
            data_path = os.path.join(nikreader_dir, 'database.json')
        self.data = self.load_data(data_path)
        
    def load_data(self, file_path):
        with open(file_path) as file:
            content = file.read()
            data = json.loads(content)
        return data
        
    def cek_provinsi(self, nik):
        prov_code = nik[:2]
        provinces = self.data.get('provinces', {})
        return provinces.get(prov_code, 'Not found in database')

    def cek_kota(self, nik):
        city_code = nik[:4]
        cities = self.data.get('cities', {})
        return cities.get(city_code, 'Not found in database')

    def cek_kecamatan(self, nik):
        subdist_code = nik[:6]
        subdistricts = self.data.get('subdistricts', {})
        return subdistricts.get(subdist_code, 'Not found in database')

    def cek_gender(self, nik):
        gender_code = nik[6:8]
        if int(gender_code) > 40:
        	return 'Perempuan'
        else:
        	return 'Laki-Laki'

    def cek_daftar(self, nik):
        daftar_code = nik[-3:]
        return daftar_code.lstrip('0')

    def cek_tanggal_lahir(self, nik):
        tgl = int(nik[6:8])
        if tgl > 40:
        	tanggal = tgl-40
        	return tanggal
        else:
        	return tgl

    def cek_bulan_lahir(self, nik):
        bln = nik[8:10]
        return bln

    def cek_tahun_lahir(self, nik):
        thn = int(nik[10:12])
        tahun = 2000 + thn if thn <= 23 else 1900 + thn
        return tahun
    
Database()