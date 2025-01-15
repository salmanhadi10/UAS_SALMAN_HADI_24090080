class Buah:
    def __init__(self):
        self.nama = []
        self.warna = []
        self.rasa = []

    def setnama(self,item):
        self.nama = item
    def setwarna(self,item2):
        self.warna = item2
    def setrasa(self,item3):
        self.rasa = item3


    def information(self):
        return f"Nama Buah : {self.nama} | Warna Buah : {self.warna} | Rasa Buah : {self.rasa}"
    
buah_satu = Buah()
buah_satu.setnama("Apel")
buah_satu.setwarna("Merah")
buah_satu.setrasa("Manis")
print(buah_satu.information())
buah_dua = Buah()
buah_dua.setnama(" Sirsak")
buah_dua.setwarna("Putih")
buah_dua.setrasa("Asam")
print(buah_dua.information())