import json

with open("aturan_baterai.json", "r", encoding="utf-8") as file:
    data = json.load(file)

aturan = data["aturan"]

pertanyaan = {
    "layar_terlalu_terang": "1. Apakah kecerahan layar HP sering tinggi? (y/n): ",
    "banyak_aplikasi_berjalan": "2. Apakah banyak aplikasi berjalan di latar belakang? (y/n): ",
    "sinyal_lemah": "3. Apakah sinyal HP sering lemah? (y/n): ",
    "fitur_konektivitas_aktif": "4. Apakah Wi-Fi, Bluetooth, atau GPS sering aktif saat tidak diperlukan? (y/n): ",
    "baterai_menurun_dari_biasanya": "5. Apakah daya tahan baterai menurun dibandingkan biasanya? (y/n): ",
    "baru_memperbarui_sistem": "6. Apakah HP baru saja memperbarui sistem? (y/n): "
}

fakta = []

print("=" * 55)
print("SISTEM PAKAR BATERAI SMARTPHONE")
print("=" * 55)
print("Identifikasi kemungkinan penyebab dan rekomendasi")
print("Jawab setiap pertanyaan dengan y (ya) atau n (tidak).\n")

for kondisi, teks in pertanyaan.items():
    jawaban = input(teks).lower().strip()

    while jawaban != "y" and jawaban != "n":
        print("Jawaban tidak valid. Masukkan y atau n.")
        jawaban = input(teks).lower().strip()

    if jawaban == "y":
        fakta.append(kondisi)

kesimpulan = []
aturan_digunakan = []

ada_kesimpulan_baru = True

while ada_kesimpulan_baru:
    ada_kesimpulan_baru = False

    for rule in aturan:
        kondisi_terpenuhi = True

        for syarat in rule["jika"]:
            if syarat not in fakta:
                kondisi_terpenuhi = False

        if kondisi_terpenuhi and rule["maka"] not in fakta:
            fakta.append(rule["maka"])
            kesimpulan.append(rule["maka"])
            aturan_digunakan.append(rule)
            ada_kesimpulan_baru = True

print("\n" + "=" * 55)
print("RINGKASAN KONDISI PENGGUNA")
print("=" * 55)

jumlah_ya = 0

for kondisi in pertanyaan:
    if kondisi in fakta:
        print("- " + kondisi.replace("_", " ").capitalize())
        jumlah_ya += 1

if jumlah_ya == 0:
    print("Tidak ada kondisi positif yang dilaporkan.")

print("\n" + "=" * 55)
print("HASIL ANALISIS SISTEM PAKAR")
print("=" * 55)

if len(aturan_digunakan) == 0:
    print("Belum ada kesimpulan yang dapat dihasilkan.")
    print("Tidak ada aturan yang cocok dengan jawaban pengguna.")
    print("Hal ini bukan berarti baterai pasti dalam kondisi baik.")

else:
    nomor = 1

    for rule in aturan_digunakan:
        if rule["jenis"] == "faktor":
            print("\nFAKTOR TERIDENTIFIKASI", nomor)
        elif rule["jenis"] == "kombinasi":
            print("\nHASIL PENALARAN GABUNGAN", nomor)
        else:
            print("\nPEMERIKSAAN LANJUTAN", nomor)

        print("Nama        :", rule["nama"])
        print("Penjelasan  :", rule["penjelasan"])
        print("Aturan      :", rule["id"])
        print("IF          :", " DAN ".join(rule["jika"]))
        print("THEN        :", rule["maka"])
        print("Rekomendasi :", rule["rekomendasi"])

        nomor += 1

print("\n" + "=" * 55)
print("RINGKASAN PROSES FORWARD CHAINING")
print("=" * 55)
print("Jumlah jawaban YA       :", jumlah_ya)
print("Jumlah aturan digunakan :", len(aturan_digunakan))
print("Jumlah kesimpulan baru  :", len(kesimpulan))

if len(aturan_digunakan) > 0:
    print("Urutan aturan:")
    urutan = []

    for rule in aturan_digunakan:
        urutan.append(rule["id"])

    print(" -> ".join(urutan))

