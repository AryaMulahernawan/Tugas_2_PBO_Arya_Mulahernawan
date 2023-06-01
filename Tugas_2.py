class Mahasiswa:  
    # ini merupakan kelas Mahasiswa
    def __init__(self, nama, nim, jurusan): 
        # method init ini berfungsi untuk menganalisis objek mahasiswa yang atributnya adalah nama,nim,dan jurusan. di kelas Mahasiswa memiliki atribut nama,nim,dan jurusan. 
        self.nama = nama            
        # kode ini merupakan bagian dari metode __init__() dalam kelas Mahasiswa.,Kode ini digunakan untuk menginisialisasi atribut nama dari objek mahasiswa dengan nilai yang diberikan saat objek dibuat.
        self.nim = nim
         # kode ini merupakan bagian dari metode __init__() dalam kelas Mahasiswa.,Kode ini digunakan untuk menginisialisasi atribut nim dari objek mahasiswa dengan nilai yang diberikan saat objek dibuat.
        self.jurusan = jurusan
         # kode ini merupakan bagian dari metode __init__() dalam kelas Mahasiswa.,Kode ini digunakan untuk menginisialisasi atribut jurusan dari objek mahasiswa dengan nilai yang diberikan saat objek dibuat.

    def tampilkan_info(self):  
         # sedangkan method tampilkan_info ini untuk mecetak informasi mahasiswa nama,nim,dan nama_jurusan dari objek jurusan .
        print("1. Nama   : ", self.nama)
        # kode merupakan bagian dari metode tampilkan_info , kode ini digunakan untuk mencetak kata "Nama: " diikuti oleh nilai atribut nama dari objek mahasiswa.
        print("   NIM    : ", self.nim)
         # kode merupakan bagian dari metode tampilkan_info , kode ini digunakan untuk mencetak kata "NIM: " diikuti oleh nilai atribut nim dari objek mahasiswa.
        print("   Jurusan: ", self.jurusan.nama_jurusan)
         # kode merupakan bagian dari metode tampilkan_info , kode ini digunakan untuk mencetak kata "Jurusan: " diikuti oleh nilai atribut nama_jurusan dari objek jurusan.


class Jurusan:   
     # ini merupakan kelas Jurusan            
    def __init__(self, nama_jurusan):   # kelas ini juga memiliki 3 method  
             # yang pertama Method __init__ digunakan untuk menginisialisasi objek jurusan dengan atribut nama_jurusan dan membuat daftar kosong untuk daftar_mahasiswa. di kelas Jurusan memiliki atribut nama_jurusan dan daftar_mahasiswa.
        self.nama_jurusan = nama_jurusan    
        self.daftar_mahasiswa = []         

    def tambah_mahasiswa(self, mahasiswa):         
         # yang kedua Methode tambah_mahasiswa digunakan untuk menambahkan objek Mahasiswa ke dalam daftar mahasiswa jurusan.
        self.daftar_mahasiswa.append(mahasiswa)

    def tampilkan_daftar_mahasiswa(self):         
          # dan yang terakhir Methode tampilkan_daftar_mahasiswa() digunakan untuk mencetak daftar mahasiswa yang terdaftar dalam jurusan.
        print("Daftar Mahasiswa Jurusan", self.nama_jurusan)
        # digunakan utntuk mencetak kalimat Daftar Mahasiswa Jurusan dan mengambil objek dari atribut nama_jurusan.
        for mahasiswa in self.daftar_mahasiswa:
            mahasiswa.tampilkan_info()


class Universitas:   
     # ini merupakan kelas Universitas
    def __init__(self, nama_universitas):     # sama seperti kelas jurusan ,kelas Universitas juga mempunyai tiga method
        #  yang pertama Methode __init__() digunakan untuk menginisialisasi objek universitas dengan atribut nama_universitas dan membuat daftar kosong untuk daftar_jurusan.          
        self.nama_universitas = nama_universitas       
        # kode ini masih merupakan 
        self.daftar_jurusan = []

    def tambah_jurusan(self, jurusan):                
          # yang kedua Methode tambah_jurusan() digunakan untuk menambahkan objek Jurusan ke dalam daftar jurusan universitas.
        self.daftar_jurusan.append(jurusan)

    def tampilkan_daftar_jurusan(self):                
         # Methode tampilkan_daftar_jurusan() digunakan untuk mencetak daftar jurusan yang ada di universitas.
        print("Daftar Jurusan di", self.nama_universitas)
        for jurusan in self.daftar_jurusan:
            print(jurusan.nama_jurusan)

xyz_university = Universitas("XYZ University")                          
 # Objek xyz_university dibuat sebagai objek Universitas dengan nama "XYZ University" menggunakan Universitas("XYZ University").
teknik_informatika = Jurusan("Teknik Informatika")                       
# Objek teknik_informatika dibuat sebagai objek Jurusan dengan nama "Teknik Informatika" menggunakan Jurusan("Teknik Informatika").
xyz_university.tambah_jurusan(teknik_informatika)                       
# Objek teknik_informatika ditambahkan ke dalam daftar jurusan di xyz_university menggunakan metode tambah_jurusan().
mahasiswa1 = Mahasiswa("Arya Mulahernawan", "G1A022029", teknik_informatika)       
 # Objek mahasiswa dibuat sebagai objek Mahasiswa dengan nama "Arya Mulahernawan", NIM "G1A022029", dan dihubungkan dengan jurusan teknik_informatika.
teknik_informatika.tambah_mahasiswa(mahasiswa1)                         
# Objek mahasiswa1 ditambahkan ke dalam daftar mahasiswa di teknik_informatika menggunakan metode tambah_mahasiswa().
xyz_university.tampilkan_daftar_jurusan()                              
 # Methode tampilkan_daftar_jurusan() pada objek xyz_university dipanggil untuk mencetak daftar jurusan yang ada di Universitas XYZ.
teknik_informatika.tampilkan_daftar_mahasiswa()                       
  # kode Methode tampilkan_daftar_mahasiswa() pada objek teknik_informatika dipanggil untuk mencetak daftar mahasiswa yang telah terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.
