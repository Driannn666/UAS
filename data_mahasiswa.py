class DataMahasiswa:
    def __init__(self):
        self.data = []
    
    def tambah(self, nim, nama, nilai):
        mahasiswa = {
            'nim': nim,
            'nama': nama,
            'nilai': nilai,
            'grade': self.hitung_grade(nilai)
        }
        self.data.append(mahasiswa)
    
    def hitung_grade(self, nilai):
        if nilai >= 85:
            return 'A'
        elif nilai >= 70:
            return 'B'
        elif nilai >= 60:
            return 'C'
        elif nilai >= 50:
            return 'D'
        else:
            return 'E'
    
    def get_data(self):
        return self.data
