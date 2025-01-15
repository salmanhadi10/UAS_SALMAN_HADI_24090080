def data():
    mahasiswa = [] 
    
    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ") 
        mahasiswa.append({"NIM": nim, "Nama": nama})
        tambah = input("Ingin tambah lagi? (ya/tidak): ").lower()
        if tambah != 'ya':
            break  

   
    print("====Data Mahasiswa=======")
    for data in mahasiswa:
        print(f"NIM: {data['NIM']}")
        print(f"Nama: {data['Nama']}")

data()
