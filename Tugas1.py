import random

# ==============================================
# DATA BARU - SEMUA KATA PANJANGNYA = 8 HURUF
# ==============================================
kamus = [
    "SIPAKAMA",   # 8
    "SIPANNAI",   # 8
    "SIPAKASI",   # 8
    "SIPATANA",   # 8
    "SIPAKATA",   # 8
    "SIPAKAJI",   # 8
    "SIPARATA",   # 8
    "MASSIPAA",   # ✅ Diperbaiki dari MASSIPA → jadi 8 huruf
    "SIPAKADE",   # 8
    "SIPAKARA"    # 8
]

TARGET = "SIPAKATA"       # Panjang = 8
TITIK_POTONG = 6          # Setelah huruf ke-6
# ==============================================

populasi = kamus.copy()

fitness = []
probabilitas = []
interval = []

parent1 = ""
parent2 = ""
child1 = ""
child2 = ""
hasil_mutasi = ""

# FUNGSI HITUNG FITNESS + PENGECEKAN PANJANG
def hitung_fitness(kata):
    if len(kata) != len(TARGET):
        return 0, 0  # Jika panjang beda, anggap tidak cocok
    benar = 0
    for i in range(len(TARGET)):
        if kata[i] == TARGET[i]:
            benar += 1
    return benar / len(TARGET), benar

# MENU 1
def tampil_kamus():
    print("\n=== KAMUS ===")
    for i, k in enumerate(kamus, 1):
        print(i, ".", k)

# MENU 2
def cari_kata():
    kata = input("Masukkan kata : ").upper()
    if kata in kamus:
        print("Kata ditemukan.")
    else:
        print("Kata tidak ditemukan.")

# MENU 3 & 5
def proses_fitness():
    global fitness
    fitness = []
    print("\n=== HASIL FITNESS ===")
    total = 0
    for i, kata in enumerate(populasi):
        f, benar = hitung_fitness(kata)
        fitness.append(f)
        total += f
        print(f"I{i+1}  {kata}  Huruf Benar={benar}  Fitness={f:.4f}")
    print("\nTotal Fitness =", round(total, 4))

# MENU 6
def roulette():
    global probabilitas, interval, parent1, parent2
    total = sum(fitness)
    if total == 0:
        print("❌ Semua fitness nol, tidak bisa lanjut.")
        return
    probabilitas = []
    interval = []
    kumulatif = 0
    print("\n=== ROULETTE WHEEL ===")
    for i in range(len(populasi)):
        p = fitness[i] / total
        probabilitas.append(p)
        awal = kumulatif
        kumulatif += p
        interval.append((awal, kumulatif))
        print(f"I{i+1}  P={p:.4f}  Interval=({awal:.4f} - {kumulatif:.4f})")
    r1 = random.random()
    r2 = random.random()
    print("\nRandom 1 =", round(r1, 4))
    print("Random 2 =", round(r2, 4))
    for i in range(len(interval)):
        if interval[i][0] <= r1 <= interval[i][1]:
            parent1 = populasi[i]
    for i in range(len(interval)):
        if interval[i][0] <= r2 <= interval[i][1]:
            parent2 = populasi[i]
    print("\nParent 1 =", parent1)
    print("Parent 2 =", parent2)

# MENU 7
def crossover():
    global child1, child2
    titik = TITIK_POTONG
    child1 = parent1[:titik] + parent2[titik:]
    child2 = parent2[:titik] + parent1[titik:]
    print("\n=== CROSSOVER ===")
    print("Titik Potong :", titik)
    print("Parent 1     :", parent1)
    print("Parent 2     :", parent2)
    print("Child 1      :", child1)
    print("Child 2      :", child2)

# MENU 8
def mutasi():
    global hasil_mutasi
    hasil_mutasi = list(child2)
    print("\n=== MUTASI ===")
    posisi_salah = []
    for i in range(len(TARGET)):
        if hasil_mutasi[i] != TARGET[i]:
            posisi_salah.append(i)
    if len(posisi_salah) == 0:
        hasil_mutasi = "".join(hasil_mutasi)
        print("✅ Tidak perlu mutasi, kata sudah sesuai target.")
        return
    posisi = random.choice(posisi_salah)
    print("Posisi Mutasi :", posisi + 1)
    print("Sebelum       :", "".join(hasil_mutasi))
    hasil_mutasi[posisi] = TARGET[posisi]
    hasil_mutasi = "".join(hasil_mutasi)
    print("Sesudah       :", hasil_mutasi)
    f, benar = hitung_fitness(hasil_mutasi)
    print("Huruf Benar   :", benar)
    print("Fitness       :", round(f, 4))

# MENU 9
def generasi():
    print("\n=== GENERASI BARU ===")
    f1, b1 = hitung_fitness(child1)
    f2, b2 = hitung_fitness(hasil_mutasi)
    print("Child 1")
    print(child1)
    print(f"Fitness = {round(f1,4)} | Huruf Benar = {b1}")
    print()
    print("Child 2")
    print(hasil_mutasi)
    print(f"Fitness = {round(f2,4)} | Huruf Benar = {b2}")
    if hasil_mutasi == TARGET:
        print("\n🎉 TARGET BERHASIL DITEMUKAN! Kata:", TARGET)
    else:
        print("\n⚠️ Belum mencapai target, ulangi proses.")

# MENU UTAMA
while True:
    print("\n==============================")
    print("   KAMUS BAHASA DAERAH")
    print("   ALGORITMA GENETIKA")
    print("==============================")
    print("1. Tampilkan Kamus")
    print("2. Cari Kata")
    print("3. Jalankan Algoritma Genetika")
    print("4. Tampilkan Populasi")
    print("5. Hasil Fitness")
    print("6. Seleksi Roulette")
    print("7. Cross Over")
    print("8. Mutasi")
    print("9. Generasi Baru")
    print("10. Keluar")
    pilih = input("\nPilih Menu : ")
    if pilih == "1":
        tampil_kamus()
    elif pilih == "2":
        cari_kata()
    elif pilih == "3":
        print("\nAlgoritma Genetika Dimulai...")
        proses_fitness()
    elif pilih == "4":
        print("\n=== POPULASI ===")
        for p in populasi:
            print(p)
    elif pilih == "5":
        proses_fitness()
    elif pilih == "6":
        if len(fitness) == 0:
            print("⚠️ Jalankan dulu menu 5 untuk menghitung fitness.")
            proses_fitness()
        roulette()
    elif pilih == "7":
        if parent1 == "" or parent2 == "":
            print("⚠️ Jalankan dulu menu 6 untuk mendapatkan parent.")
        else:
            crossover()
    elif pilih == "8":
        if child1 == "" or child2 == "":
            print("⚠️ Jalankan dulu menu 7 untuk mendapatkan child.")
        else:
            mutasi()
    elif pilih == "9":
        if hasil_mutasi == "":
            print("⚠️ Jalankan dulu menu 8 untuk proses mutasi.")
        else:
            generasi()
    elif pilih == "10":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("❌ Pilihan tidak tersedia, coba lagi.")