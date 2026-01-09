class ViewMahasiswa:
    def tampilkan_menu(self):
        print("\n" + "="*50)
        print("SISTEM MANAJEMEN DATA MAHASISWA")
        print("="*50)
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Keluar")
        print("="*50)
    
    def tampilkan_tabel(self, data):
        if not data:
            print("\nBelum ada data mahasiswa.")
            return
        
        print("\n" + "="*80)
        print(f"{'NIM':<15} {'NAMA':<25} {'NILAI':<10} {'GRADE':<10}")
        print("="*80)
        for mhs in data:
            print(f"{mhs['nim']:<15} {mhs['nama']:<25} {mhs['nilai']:<10} {mhs['grade']:<10}")
        print("="*80)
    
    def tampilkan_pesan(self, pesan):
        print(f"\n{pesan}")
