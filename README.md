# Albion Storage
[Application Link](https://albionstorage.adaptable.app/main/)

## _Step-by-step_ pengerjaan tugas
### 1. Membuat sebuah proyek Django baru
Setup library pada berkas `requirements.txt` dengan menambahkan beberapa _dependencies_,
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
kemudian saya menginstall tanpa Virtual Environment dengan, 
```
pip install -r requirements.txt
```
untuk membuat proyek Django, maka saya menggunakan command,
```
django-admin startproject NAME .
```
dilanjutkan dengan mengkonfigurasi pengizinan semua host pada `settings.py`, maka program sudah siap dijalankan (wajib dilakukan untuk mengakses web django lewat `http://localhost:8000/hello`,
```
python manage.py runserver
```
### 2. Membuat aplikasi dengan nama main
Saya membuat aplikasi baru dengan command,
```
python manage.py startapp main
```
setelah itu saya mendaftarkan main ke dalam daftar aplikasi pada `settings.py`
### 3. Melakukan routing proyek agar dapat menjalankan aplikasi
Untuk melakukan routing, maka diperlukan berkas `urls.py` yang bertanggung jawab mengatur rute URL yang terkait dengan aplikasi `main`, berikut isi `urls.py`,
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
### 4. Membuat model pada aplikasi
Aplikasi ini bertujuan memberi ringkasan atas detail penyimpanan `item` pada suatu `characterID`, maka dari itu saya membarukan `models.py` dengan,
'''
name = models.CharField(max_length=255)
class = models.CharField(max_length=255)
accountID = models.CharField(max_length=255)
balance = models.IntegerField()
item = models.CharField(max_length=255)
description = models.TextField()
itemPower = models.IntegerField()
tier = models.IntegerField()
amount = models.IntegerField()
place = models.CharField(max_length=255)
price = models.IntegerField()
'''
### 5. Membuat fungsi pada `views.py` untuk dikembalikan ke dalam template HTML
Agar model yang telah diinstansiasi pada `models.py` dapat memiliki nilai yang akan digunakan pada template html, maka saya memberikan nilai pada tiap model seperti berikut,
'''
'name' = 'Hanan Adipratama',
'class' = 'PBP B',
'accountID': 'RigenMengaji',
'balance' : '15000000',
'item' : 'Cursed Staff',
'description': 'The Adept\'s Great Cursed Staff is a Tier 4 Cursed Staff which may be obtained by crafting or via the Market Place',
'itemPower' : '800',
'tier' : '4',
'amount' : '1',
'place' : 'Lymhurst Bank',
'price' : '2000'
'''
agar dapat dirender maka perlu kode berikut,
```
return render(request, "main.html", context)
```
### Melakukan deployment ke Adaptable
Setelah projek difinalisasi maka saya melakukan push ke github yang nantinya akan dihubungkan ke Adaptable dengan spesifikasi `Python App Template`, database `PostgreSQL`, lalu menyesuaikan dengan versi python saya yang dicek melalui `python --version`, kemudian memasukkan `python manage.py migrate && gunicorn NAME.wsgi` pada `Start Command`, menentukan nama aplikasi, dan checklist `HTTP Listener on PORT`

## Bagan Aplikasi Berbasis Django
![google](https://www.google.com/url?sa=i&url=https%3A%2F%2Flearnbatta.com%2Fblog%2Funderstanding-request-response-lifecycle-in-django-29%2F&psig=AOvVaw0E45IreeNH_5Te-wmwz4Ab&ust=1694656130148000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCODsspe8poEDFQAAAAAdAAAAABAE)
1. _Client_ mengirimkan permintaan HTTP/HTTPS ke server Django.
2. Permintaan diterima oleh web server.
3. Web server meneruskan permintaan ke server WSGI atau menanganinya sendiri.
3. Server WSGI meneruskan permintaan ke aplikasi Django.
4. Siklus _request-response_ Django melibatkan:
    a. Request Middleware, penanganan permintaan pertama kali sesuai urutan
    b. Router URL, mencocokkan jalur URL dengan pola yang sesuai
    c. Views, mengolah logika dan mengirimkan permintaan ke Middleware Context
    d. Context Processors, menambahkan data konteks yang diperlukan untuk Renderer Template
    e. Renderer Template, merender template untuk menghasilkan tanggapan HTTP
    f. Response Middleware, memproses permintaan sebelum dikirimkan kembali ke klien
5. _Client_ memproses dan menampilkan tanggapan yang diterima dari server kepada pengguna akhir.
## Mengapa Menggunakan Virtual Environment
Kita menggunakan virtual environment pada pengembangan aplikasi berbasis Django agar bisa mengisolasi dan mengelola dependensi berikut dengan paket Python secara terpisah untuk setiap proyek, sehingga mencegah konflik dan memastikan kestabilan lingkungan pengembangan.

Apakah bisa melakukan pengembangan aplikasi berbasis django tanpa virtual environment? **BISA,** namun dengan kekurangan memungkinkan terjadinya konflik dependensi, tidak terisolasi, kurang fleksibel, dan masalah manajemen versi python antar file yang berbeda.
## Apa itu MVC, MVT, MVVM
**MVC (Model-View-Controller):**
  Model: Bertanggung jawab untuk mengelola data dan logika bisnis.
  View: Menangani tampilan data dan berinteraksi dengan pengguna.
  Controller: Menangani permintaan dari pengguna, memproses input, dan mengarahkan perubahan ke Model atau View yang sesuai.
  Perbedaan: MVC adalah arsitektur yang digunakan terutama dalam kerangka kerja web seperti Ruby on Rails dan Laravel. Model mengatur data, View menampilkan data, dan Controller mengatur logika bisnis dan interaksi pengguna.
**MVT (Model-View-Template):**
  Model: Sama dengan konsep dalam MVC, mengelola data dan logika bisnis.
  View: Menangani tampilan data dan berinteraksi dengan pengguna, tetapi dalam kerangka kerja Django, View juga berfungsi sebagai Controller dalam MVC.
  Template: Menangani bagian tampilan, seperti markup HTML, dan dapat digunakan untuk merender data dari View.
  Perbedaan: MVT adalah varian dari MVC yang digunakan dalam kerangka kerja web Django. Peran View di Django mencakup fungsi dari Controller dalam MVC, sementara Template bertanggung jawab untuk tampilan.
**MVVM (Model-View-ViewModel):**
  Model: Seperti pada MVC, mengelola data dan logika bisnis.
  View: Bertanggung jawab untuk tampilan, seperti dalam MVC.
  ViewModel: Menyediakan perantara antara Model dan View. Ini mengubah data Model ke format yang dapat ditampilkan oleh View dan menerima input dari View untuk memperbarui Model.
  Perbedaan: MVVM adalah arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis klien (seperti aplikasi desktop atau aplikasi mobile). ViewModel adalah perbedaan utama, yang memisahkan View dan Model dengan memasukkan lapisan perantara.
