# SOAL 2: Sistem Penilaian & Kelulusan Akademik SmartCampus

print("Simulasi Akademik Soal 2")

tugas = int(input("Masukkan nilai tugas: "))
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))
kehadiran = int(input("Masukkan Kehadiran (%): "))
pelanggaran_berat = input("Ada Pelanggaran Berat? (YA/TIDAK): ").upper()
organisasi = input("Aktif Organisasi? (YA/TIDAK): ").upper()

NA = int((tugas * 0.25) + (uts * 0.35) + (uas * 0.40))

status = ""
predikat = ""
hak_beasiswa = "Tidak Ada"

if NA < 60 or kehadiran < 75 or pelanggaran_berat == "YA":
    status = "Tidak Lulus"
    predikat = "Harus Mengulang"
    hak_beasiswa = "Tidak Ada"
else:
    status = "Lulus"
    if NA >= 85 and kehadiran >= 85:
        predikat = "Cumlaude"
        hak_beasiswa = "Diterima Utama"
    elif NA >= 70:
        predikat = "Memuaskan"
        if organisasi == "YA":
            hak_beasiswa = "Diterima Pendukung"
    else:
        predikat = "Cukup"

print("\n" + "="*40)
print(f"Nilai Akhir: {NA} | Kehadiran: {kehadiran}% | Pelanggaran: {pelanggaran_berat} | Organisasi: {organisasi}")
print(f"Status: {status} | Predikat: {predikat} | Hak Beasiswa: {hak_beasiswa}")
    
if predikat == "Cumlaude":
    print("\nStatus: Semua syarat nilai >= 85, kehadiran >= 85%, dan bersih dari pelanggaran terpenuhi.")
print("="*40)