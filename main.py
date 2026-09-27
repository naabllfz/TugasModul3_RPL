# Tugas Modul 3
# Nabil Afzaal_F5212520061
# Menghitung Nilai Akhir dan Predikat Mahasiswa

def minta_nilai(label):
    while True:
        try:
            nilai = float(input(f"Masukkan nilai {label} (0-100): "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 dan 100. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def tentukan_predikat(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    else:
        return "E"

def main():
    print("Program Menghitung Nilai Akhir dan Predikat Mahasiswa")
    
    # Meminta input nilai dari pengguna
    nilai_tugas = minta_nilai("tugas")
    nilai_uts = minta_nilai("UTS")
    nilai_uas = minta_nilai("UAS")
    
    # Menghitung nilai akhir
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
    
    # Menentukan predikat
    predikat = tentukan_predikat(nilai_akhir)
    
    # Menampilkan hasil
    print(f"\nNilai Akhir: {nilai_akhir:.2f}")
    print(f"Predikat: {predikat}")

if __name__ == "__main__":
    main()