from data_mahasiswa import DataMahasiswa
from view_mahasiswa import ViewMahasiswa

class ProcessMahasiswa:
    def __init__(self):
        self.data = DataMahasiswa()
        self.view = ViewMahasiswa()
    
    def validasi_nim(self, nim):
        if not nim:
            raise ValueError("NIM tidak boleh kosong!")
        if not nim.isdigit():
            raise ValueError("NIM harus berupa angka!")
        if len(nim) < 5:
            raise ValueError("NIM minimal 5 digit!")
        return True
    
    def validasi_nama(self, nama):
        if not nama:
            raise ValueError("Nama tidak boleh kosong!")
        if len(nama) < 3:
            raise ValueError("Nama minimal 3 karakter!")
        return True
    
    def validasi_nilai(self, nilai_str):
        try:
            nilai = float(nilai_str)
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus antara 0-100!")
            return nilai
        except ValueError:
            raise ValueError("Nilai harus berupa angka!")
    
    def input_mahasiswa(self):
        try:
            print("\n--- Input Data Mahasiswa ---")
            nim = input("Masukkan NIM: ").strip()
            self.validasi_nim(nim)
            
            nama = input("Masukkan Nama: ").strip()
            self.validasi_nama(nama)
            
            nilai_str = input("Masukkan Nilai (0-100): ").strip()
            nilai = self.validasi_nilai(nilai_str)
            
            self.data.tambah(nim, nama, nilai)
            self.view.tampilkan_pesan("✓ Data mahasiswa berhasil ditambahkan!")
            
        except ValueError as e:
            self.view.tampilkan_pesan(f"✗ Error: {str(e)}")
    
    def tampilkan_data(self):
        data = self.data.get_data()
        self.view.tampilkan_tabel(data)
    
    def jalankan(self):
        while True:
            self.view.tampilkan_menu()
            pilihan = input("Pilih menu (1-3): ").strip()
            
            if pilihan == '1':
                self.input_mahasiswa()
            elif pilihan == '2':
                self.tampilkan_data()
            elif pilihan == '3':
                self.view.tampilkan_pesan("Terima kasih! Program selesai.")
                break
            else:
                self.view.tampilkan_pesan("✗ Pilihan tidak valid! Silakan pilih 1-3.")
