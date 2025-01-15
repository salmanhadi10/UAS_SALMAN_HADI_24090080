from soal_3_md.py import Stack

antrean_satu = Stack()
antrean_satu.push("JOKO")
antrean_satu.push("AJI")
antrean_satu.push("HARIS")

while True:
    for i, data in enumerate(antrean_satu.items,1):
        print(f'Antrean Ke-{i} {data}')
    antrean_satu.tampilan()
    pilih = int(input('Masukan Pilihan : '))
    print("="*50)
    if pilih == 1:
        nama = str(input("Masukan Nama :"))
        antrean_satu.push(nama.capitalize())
        print("="*100)
    if pilih == 2:
        antrean_satu.pop()
    if pilih == 3:
        keluar = str("Ingin Keluar Program? (Ya/Tidak) : ").upper()
        if keluar == "Ya":
            break