# Albion Storage
[Application Link](https://albionstorage.adaptable.app/main/)

# TUGAS 2
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
```
name = models.CharField(max_length=255)
date_added = models.DateField(auto_now_add=True)
description = models.TextField()
amount = models.IntegerField()
```
### 5. Membuat fungsi pada `views.py` untuk dikembalikan ke dalam template HTML
Agar model yang telah diinstansiasi pada `models.py` dapat memiliki nilai yang akan digunakan pada template html, maka saya memberikan nilai pada tiap model seperti berikut,
```
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
```
agar dapat dirender maka perlu kode berikut,
```
return render(request, "main.html", context)
```
### Melakukan deployment ke Adaptable
Setelah projek difinalisasi maka saya melakukan push ke github yang nantinya akan dihubungkan ke Adaptable dengan spesifikasi `Python App Template`, database `PostgreSQL`, lalu menyesuaikan dengan versi python saya yang dicek melalui `python --version`, kemudian memasukkan `python manage.py migrate && gunicorn NAME.wsgi` pada `Start Command`, menentukan nama aplikasi, dan checklist `HTTP Listener on PORT`

## Bagan Aplikasi Berbasis Django
![google](https://learnbatta.com/assets/images/django/request_response_lifecycle_Django.png)
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
1. **MVC (Model-View-Controller):**
   MVC merupakan Model View yang menangani permintaan dari pengguna, memproses input, dan mengarahkan perubahan ke Model atau View yang sesuai. Yang membedakan MVC adalah arsitektur yang digunakan terutama dalam kerangka kerja web seperti Ruby on Rails dan Laravel. Model mengatur data, View menampilkan data, dan Controller mengatur logika bisnis dan interaksi pengguna.
2. **MVT (Model-View-Template):**
   MVT adalah Model View yang menangani bagian tampilan, seperti _markup_ HTML, dan dapat digunakan untuk merender data dari View. Yang membedakan MVT adalah varian dari MVC yang digunakan dalam kerangka kerja web Django. Peran View di Django mencakup fungsi dari Controller dalam MVC, sementara Template bertanggung jawab untuk tampilan.
3. **MVVM (Model-View-ViewModel):**
   MVVM merupakan Model View yang menyediakan perantara antara Model dan View. Dengan kata lain mengubah data Model ke format yang dapat ditampilkan oleh View dan menerima input dari View untuk memperbarui Model. Yang membedakan MVVM adalah arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis klien (seperti aplikasi desktop atau aplikasi mobile). ViewModel adalah perbedaan utama, yang memisahkan View dan Model dengan memasukkan _middle-layer_.

# TUGAS 3
## Perbedaan POST dan GET dalam Django
Form POST dan form GET adalah dua metode pengiriman data dari browser ke server dalam pengembangan web dengan menggunakan protokol HTTP.

**POST** <br>
Post biasa digunakan ketika ingin mengirim data yang akan dimasukkan ke dalam database, melakukan tindakan yang memengaruhi data di server, atau mengirimkan data yang sensitif. Berikut poin-poin untuk memperjelas:
1. Data dikirimkan dalam badan permintaan HTTP. Karena tidak tampil langsung di URL, sehingga cocok untuk mengirim data yang sensitif. Selain itu juga membuat URL tetap bersih dan dapat dibaca oleh manusia.
2. Menghindari penyimpanacan cache.
3. Tidak memiliki batas ukuran data yang dapat dikirimkan, cocok untuk mengirim data besar atau kompleks

**GET** <br>
Metode GET umumnya digunakan untuk mengambil data dari server tanpa mengubahnya, seperti pencarian atau pengambilan halaman. Berikut poin-poin untuk memperjelas:
1. Data dikirimkan sebagai bagian dari URL. Karena tampil langsung di URL, sehingga tidak cocok untuk mengirim data yang sensitif. Selain itu juga membuat URL panjang sesuai dengan parameter yang digunakan.
2. Memungkinkan penyimpanan cache, namun sensitif akan perubahan data yang dinamis.
3. Memiliki batas ukuran data yang dapat dikirimkan, cocok untuk mengirim data yang relatif kecil.

## Perbedaan utama XML, JSON, dan HTML dalam konteks pengeriman data
**XML**
- Penggunaan: Umumnya digunakan untuk pertukaran data antar sistem atau aplikasi.
- Struktur: Data dalam XML dikelompokkan dalam elemen, dan setiap element memiliki tag pembuka dan penutup. Memungkinkan pendifinisian data yang terstruktur dan fleksibel. co:
```
<person>
    <name>Hanan Adipratama</name>
    <age>19</age>
</person>
```
- Keunggulan: Self-descriptive, mendukung validasi melalui DTD atau XML Schema, dapat digunakan untuk data dengan struktur yang kompleks.

**JSON**
- Penggunaan: JSON didesain untuk pertukaran data ringan antar sistem dan bahasa pemrograman.
- Struktur: Data dalam JSON berformat teks yang terdiri dari pasangan "key-value". co:
```
{
"name": "Hanan Adipratama",
"age": 19
}
```
- Keunggulan: Mudah dibaca oleh manusia dan diurai oleh mesin, efisien dalam penggunaan bandwidth, kompatibel dengan banyak bahasa pemrograman.

**HTML**
- Penggunaan: Bahasa markup yang digunakan untuk mengatur tampilan dan struktur elemen-element web di browser.
- Struktur: HTML memiliki struktur yang ditentukan dengan baik, terdiri dari elemen-element seperti `<html>`, `<head>`, `<body>`, `<p>`, `<div>`, dan banyak lagi. Ini tidak digunakan untuk pertukaran data dalam format yang kaya, tetapi untuk menampilkan konten di browser. co:
```
<tr>
    <td>Hanan Adipratama</td>
    <td>19</td>
</tr>
```
- Keunggulan: Digunakan untuk membangun tampilan halaman web, memiliki struktur yang terdefinisi dengan baik, tidak digunakan untuk pertukaran data.
<br>
Singkatnya, XML digunakan untuk merepresentasikan data dengan struktur yang kompleks, JSON digunakan untuk pertukaran data ringan antar aplikasi, dan HTML digunakan untuk membangun tampilan halaman web di browser. 

## Pertukaran data antara aplikasi web modern menggunakan JSON
1. **Ringkas dan Mudah Dibaca**: JSON memiliki format yang ringkas dan mudah dibaca oleh manusia. Data dalam JSON diwakili dalam bentuk objek dan larik yang mirip dengan struktur data yang digunakan dalam banyak bahasa pemrograman. Ini membuatnya mudah bagi pengembang untuk memahami dan mengelola data JSON.

2. **Independen Bahasa**: JSON adalah format data yang independen dari bahasa, artinya dapat digunakan dalam berbagai bahasa pemrograman. Hal ini memungkinkan aplikasi yang ditulis dalam bahasa yang berbeda untuk berkomunikasi dan berbagi data dengan mudah.

3. **Mendukung Struktur Nested Array**: JSON mendukung struktur nested array, yang memungkinkan untuk menyimpan data yang kompleks dengan mudah.

4. **Kompatibel dengan JavaScript**: JSON merujuk pada "JavaScript" dalam namanya karena formatnya mirip dengan objek JavaScript. Ini membuatnya sangat cocok untuk digunakan dalam aplikasi web yang menggunakan JavaScript sebagai bahasa pemrograman klien.

5. **Dukungan Browser Terintegrasi**: Banyak browser modern memiliki dukungan terintegrasi untuk parsing JSON. Ini memudahkan pengembang dalam mengirim data JSON dari server ke aplikasi web tanpa perlu parsing yang rumit.

6. **Mendukung RESTful APIs**: JSON sering digunakan dalam pengembangan RESTful APIs, yang merupakan pendekatan yang umum digunakan dalam pembangunan aplikasi web modern.

7. **Ringan dan Efisien**: JSON memiliki overhead yang rendah dalam representasi data, sehingga ukuran data yang dikirimkan melalui jaringan lebih kecil. Hal ini dapat mengurangi latensi dan menghemat bandwidth.

8. **Dukungan Library**: Terdapat banyak library JSON yang tersedia untuk berbagai bahasa pemrograman, yang membuat pengolahan data JSON menjadi lebih mudah dan efisien. 

## _Step-by-step_ 
### 1. Membuat Form Input Data
**(Pasal Form)** Agar user dapat memberikan input maka Saya membuat berkas baru `forms.py` dengan isi,
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description", "price"]
```
Isi dari form nantinya akan disimpan menjadi objek `Product` yang memiliki field name, amount, description, price untuk ditampilkan.

### 2. Konfigurasi `views.py`
Menambahkan library yang dibutuhkan berupa,
```
# Mengurus pasal form
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
# Mengurus pasal data menggunakan XML dan JSON
from django.http import HttpResponse
from django.core import serializers
# Mengurus perhitungan data
from django.db.models import Sum, F
```
**(Pasal Form)** Untuk menghasilkan formulir yang dapat menambahkan data produk secara otomatis, maka saya membuat function `create_product`, dengan isi
```
def create_product(request):
    # input dari user berupa request.POST dimasukkan untuk membuat product
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save() # Menyimpan product ketika valid
        return HttpResponseRedirect(reverse('main:show_main')) # redirect

    context = {'form': form}
    return render(request, "create_product.html", context)
```
Selanjutnya saya melakukan perubahan agar request pada form dapat dilanjutkan pada file `views.py` pada function `create_product`, menambahkan kode
```
...
products = Product.objects.all() # Menyimpan semua data product yang ada pada database
...
    context = {
      ...
      'products' : products, # Instansiasi product
      ...
    }

    return render(request, "main.html", context)
```
**(Pasal XML)** untuk mengurus data menggunakan XML maka saya menambahkan function `show_xml` dan `show_xml_id`
```
def show_xml(request):
    data = Product.objects.all() # Mengambil semua data product
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id) # Hanya mengambil product pada id yang dimasukkan
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
**(Pasal JSON)** untuk mengurus data menggunakan json maka saya menambahkan function `show_json` dan `show_json_id`
```
def show_json(request):
    data = Product.objects.all() # Mengambil semua data product
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
```
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id) # Hanya mengambil product pada id yang dimasukkan
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### 3. Konfigurasi HTML
Agar memudahkan strukturalisasi html, saya membuat kerangka utama pada folder `main\templates` berkas `base.html`,
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
**(Pasal Form)** Membuat berkas baru untuk mendisplay form yang akan diinput user `create_product.html`,
```
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
Untuk mendisplay form pada `main.html`,
```
...
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Amount</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.amount}}</td>
            <td>{{product.description}}</td>
            <td>{{product.price}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```
### 4. Konfigurasi Routing
Saya mengupdate import untuk mengurus pasal akses form (`create product`), pasal data pada xml (`show_xml`, `show_xml_by_id`), pasal data pada json (`show_json`, `show_json_by_id`)
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
```
**(Pasal Form)** Untuk mengakses form maka saya membuat path baru,
```
path('create-product', create_product, name='create_product'),
```
**(Pasal XML)** Untuk mengakses keseluruhan data ataupun per id pada XML maka saya membuat path baru,
```
path('xml/', show_xml, name='show_xml'),
```
```
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
```
**(Pasal JSON)** Untuk mengakses keseluruhan data ataupun per id pada JSON maka saya membuat path baru,
```
path('json/', show_json, name='show_json'), 
```
```
path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
```

### Catatan Tambahan
Saya menambahkan model berupa price pada `models.py`, 
```
class Product(models.Model):
   ...
   price = models.IntegerField()
```
Agar perubahan dapat terjadi maka perlu melakukan migrasi ulang
```
python manage.py makemigrations # Konfirmasi perubahan + Menambahkan default pada field baru untuk data yang lama
```
```
python manage.py migrate
```
Data price ini saya gunakan untuk menghitung balance pada `views.py`
```
def show_main(request):
   ...
   balance = products.aggregate(balance=Sum(F('amount') * F('price')))['balance']
   ...
   context = {
      ...
      'balance' : balance,
      ...
   }
``` 
Saya juga melakukan penghitungan item yang tersimpan, hal ini saya lakukan di `views.py`,
```
def show_main(request):
   ...
   product_count = products.count()
   ...
   context = {
      ...
      'product_count': product_count,
      ...
   }
``` 
`balance` dan `product_count` nantinya bisa dipanggil di `main.html`.

## Screenshoot Postman
### `localhost:8000`
<img width="960" alt="htmlscreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/1b59a24d-1eda-4ccb-aa21-8f01a9d15455">

### `localhost:8000/xml`
<img width="960" alt="xmlscreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/b6f9bf05-9c38-479a-8c23-a5cb0fa1533f">

### `localhost:8000/json`
<img width="960" alt="jsonscreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/0e6a9718-94e9-4616-89aa-68eb174cbac4">

### `localhost:8000/xml/[id]` (ID yang dipakai 1)
<img width="960" alt="xmlbyidscreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/29203dfd-860b-4071-9bd0-ecd2d9fac937">

### `localhost:8000/json[id]` (ID yang dipakai 1)
<img width="960" alt="jsonbyidscreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/3c44b487-9f5b-4785-b98f-65adfd8c1a87">


# TUGAS 4
## Apa itu UserCreationForm?
`UserCreationForm` adalah salah satu bentuk formulir yang disediakan oleh Django, yang digunakan untuk membuat formulir pendaftaran pengguna. Formulir ini memungkinkan pengguna untuk membuat akun baru dengan mengisi informasi seperti `username` dan `password`.
### Kelebihan
1. **Mudah digunakan**, tidak perlu menulis kode dari awal untuk mengelola proses pendaftaran karena sudah terintegrasi dengan Django's authentication system.
2. **Aman**, dilengkapi dengan validasi kata sandi yang kuat, perlindungan terhadap serangan CSRF (Cross-Site Request Forgery), dan lainnya.
3. **Dapat dikustomisasi**, meskipun sudah menjadi fitur bawaan, `UserCreationForm` masih dapat diubah dengan menambahkan bidang tambahan ke formulir, mengubah pesan kesalahan, dan lain-lain.
### Kekurangan
1. **Terbatas**, karena merupakan fitur bawaan belum tentu dapat dikustomisasi dengan fitur pendaftaran yang lebih kompleks atau persyaratan yang khusus.
2. **Tidak mendukung otentikasi pihak ketiga**, masih memerlukan integrasi dengan pustaka atau solusi tambahan untuk ekstensi seperti OAuth atau SSO.

## Autentikasi VS Otorisasi
### Autentikasi
Autentifikasi adalah proses verifikasi identitas pengguna. Tujuan autentikasi adalah **memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah pengguna yang sah**. Ini melibatkan pengenalan pengguna melalui penggunaan nama pengguna dan kata sandi atau metode otentikasi lainnya. Contohnya adalah proses memasukkan username dan password ketika hendak login.
### Otorisasi
Otorisasi adalah proses menentukan **apa yang dapat atau tidak dapat dilakukan pengguna** yang telah diautentifikasi. Tujuan otorisasi adalah memastikan bahwa pengguna yang terotentikasi hanya memiliki akses dan izin untuk melakukan tindakan tertentu dalam aplikasi. Ini melibatkan definisi peran, hak akses, dan kebijakan yang mengatur tindakan pengguna dalam aplikasi. Contohnya dalam file editor daring yang bisa mengedit file hanya pihak dengan akses tertentu sedangkan yang tidak mendapat akses hanya bisa melihat atau memberi komentar.
### Poin Penting
Sistem autentikasi dan otorisasi memungkinkan adanya,
1. **Keamanan**, dengan proses autentikasi yang menyaring kredibilitas pengguna diikuti dengan proses otoriasi yang menyaring aksesibilitas pengguna, dapat membantu melindungi baik aplikasi maupun data pengguna.
2. **Menjaga privasi**, autentikasi membantu melindungi data pribadi pengguna dengan memastikan bahwa hanya pengguna yang sah yang dapat mengakses informasi tersebut. Otorisasi memastikan bahwa pengguna hanya dapat melihat atau mengedit data yang seharusnya mereka lihat atau ubah.
3. **Mengikuti standar hukum**, autentikasi dan otorisasi seringkali diperlukan untuk memenuhi persyaratan peraturan dan kepatuhan hukum, contohnya GDPR (General Data Protection Regulation) atau di Indonesia berhubungan dengan UU PDP (Undang-Undang Perlindungan Data Pribadi)

## Apa Itu `Cookies`?
`Cookies` adalah file kecil yang disimpan pada perangkat pengguna oleh server web saat mereka mengunjungi situs web tertentu untuk keperluan web menyediakan pengalaman pengguna yang lebih baik. Yang membedakan `cookies` dengan penyempinan data lainnya adalah penyimpanan berada di sisi klien, kapasitas terbatas, dan mudah digunakan/diakses oleh browser web. Berikut adalah cara Django menggunakan `cookies` untuk mengelola data sesi pengguna:
1. **Identifikasi pengguna**, saat pengguna pertama kali mengunjungi dan melakukan autentikasi pada situs web, Django akan membuat session ID unik yang terkait dengan pengguna untuk proses identifikasi sesi pengguna.
2. **Penyimpanan data sesi**, memungkinkan adanya penyimpanan data selama sesi pengguna. Data ini dapat mencakup informasi seperti preferensi pengguna, keranjang belanja, atau status masuk pengguna. Data sesi ini disimpan di sisi server. 
3. **Pengiriman `cookies`**, setelah sesi pengguna dibuat dan data sesi disimpan, server Django akan mengirimkan session ID ini ke perangkat pengguna sebagai `cookies`. `Cookies` ini biasanya disimpan dalam browser web pengguna dan dikirimkan kembali ke server dengan setiap permintaan berikutnya.
4. **Pemulihan data sesi**,  Ketika pengguna melakukan permintaan berikutnya ke situs web, `cookies` yang berisi session ID dikirimkan ke server. Django akan menggunakan session ID ini untuk mengidentifikasi sesi pengguna yang sesuai dan mengembalikan data sesi pengguna yang relevan dari penyimpanan server. 
5. **Penghapusan data sesi**, saat pengguna keluar atau sesi berakhir, data sesi pengguna dapat dihapus dari penyimpanan server. Ini akan menghentikan akses pengguna ke data sesi tersebut.

## Keamanan Penggunaan `Cookies`
Penggunaan `cookies` dalam pengembangan web tidak selalu aman secara default,
### Resiko
1. **Kebocoran Data**, jika informasi sensitif disimpan dalam `cookies`, risiko kebocoran data dapat terjadi jika `cookies` tersebut diretas atau disusupi.
2. **Pelacakan Pengguna**, `cookies` dapat digunakan untuk melacak aktivitas pengguna secara online. Ini bisa menjadi masalah privasi jika informasi tersebut disalahgunakan.
3. **Cross-Site Scripting (XSS)**, Jika situs web memiliki celah XSS, penyerang dapat mencuri atau memanipulasi `cookies` pengguna.
4. **Cross-Site Request Forgery (CSRF)**, `cookies` dapat digunakan oleh serangan CSRF untuk memicu aksi yang tidak diinginkan pada nama pengguna yang sudah diautentikasi. 
### Pencegahan
1. **Tidak menyimpan data sensitif secara langsung** di `cookies` klien. Gunakan teknik enkripsi jika diperlukan.
2. **Tidak menggunakan `cookies` untuk penyimpanan data yang kritis**, seperti token otentikasi.
3. **Mengatur kebijakan penggunaan `cookies`** yang sesuai, seperti kebijakan SameSite dan HttpOnly.
4. **Melindungi situs web** dari celah keamanan seperti XSS dan CSRF.

## _Step-by-step_ pengerjaan tugas
### 1. Implementasi Fungsi Registrasi, Login dan Logout
Menambahkan library yang diperlukan pada `views.py`,
```
# Pasal Register
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
# Pasal Login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Pasal Logout
from django.contrib.auth import logout
```
Membuat fungsi `register`, `login_user`, dan `logout_user` pada `views.py`,
```
def register(request):
    form = UserCreationForm() # Membuat UserCreationForm dgn memasukkan QueryDict dari input user

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login') # Kembali ke page login
```
Mengupdate path pada `urls.py` untuk mengakses fungsi `register`, `login_user`, dan `logout_user`,
```
...
from main.views import register, login_user, logout_user, 
...
urlpatterns = [
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
```
Membuat `login.html` untuk page login,
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
``` 
dan `register.html` untuk page register,
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
dan mengupdate `main.html` dengan tombol logout,
```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```
agar halaman main hanya bisa diakses setelah login maka menambahkan kode pada `views.py` sebelum fungsi `show_main`,
```
@login_required(login_url='/login')
```

### 2. Menerapkan Cookies
Menyiapkan library pada `views.py`,
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```
lalu masih di file yang sama lakukan perubahan pada fungsi `login_user`,
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
pada `show_main`,
```
...
context = {
    ...
    'last_login': request.COOKIES['last_login'],
}
...
```
pada `logout_user`,
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
### 3. Menghubungkan Model `Item` dengan `User`
Mengupdate `models.py` dengan persiapan modul
```
...
from django.contrib.auth.models import User
...
```
lalu mengubah model `Product` menjadi,
```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Mengasosiakan produk dengan user
    ...
```
Melakukan perubahan pada `views.py` pada fungsi `create_product`,
```
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False) # Mencegah penimpanan langsung ke database
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```
dan pada fungsi `show_main`,
```
def show_main(request):
    products = Product.objects.filter(user=request.user) # Memfilter produk yang hanya terasosiasi dengan user yang sedang login

    context = {
        'name': request.user.username,
    ...
    }
...
```
lalu melakukan migrasi dikarenakan melakukan perubahan pada model dengan,
```
python manage.py makemigrations
```
```
python manage.py migrate
```

### 4. Membuat Dua Akun dengan Tiga Dummy Data untuk Setiap Akun Lokal
#### Akun a,
<img width="960" alt="dummyascreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/8e070547-e665-46d7-879f-0128166c2c3b">

#### Akun b,
<img width="960" alt="dummybscreenshot" src="https://github.com/hanan-collab/AlbionStorage/assets/63461469/6e240ba1-69a8-4097-8df9-d2e48c4aa72b">

### 5. Catatan Tambahan
Menambahkan button decrement amount, increment amount, dan delete product pertama-tama menambahkan library yang dibutuhkan
```
from django.shortcuts get_object_or_404
```
kemudian membuat fungsi pada `views.py`,
```
def decrement_amount(request, id):
    data = get_object_or_404(Product, pk=id)
    if data.amount > 0:
        data.amount -= 1
        data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def increment_amount(request, id):
    data = get_object_or_404(Product, pk=id)
    data.amount += 1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_product(request, id):
    data = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        data.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
kemudian mengupdate path pada `urls.py`,
```
from main.views import decrement_amount, increment_amount, delete_product

urlpatterns = [
    ...
    path('decrement_amount/<int:id>/', decrement_amount, name='decrement_amount'),
    path('increment_amount/<int:id>/', increment_amount, name='increment_amount'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
]
```
kemudian membuat button pada `main.html`,
```
...
<td>
    <form method="post" action="{% url 'main:decrement_amount' product.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-primary btn-sm">-</button>
    </form>
</td>
<td>{{ product.amount }}</td>
<td>
    <form method="post" action="{% url 'main:increment_amount' product.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-primary btn-sm">+</button>
    </form>
</td>
...
<td>
    <form method="post" action="{% url 'main:delete_product' product.id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-danger btn-sm">Delete</button>
    </form>
</td>
...
```
# TUGAS 5
## Element Selector dan Manfaatnya
Element selector memilih HTML element berdasar nama dari element tersebut. Element Selector dapat dibagi menjadi,
### 1. Selector Tag Umum (Ex: `<p>`, `<h1>`, etc):
```
p {
  font-size: 16px;
}
```
* Kegunaan pada contoh: Selector ini digunakan untuk mengubah ukuran font semua element paragraf (<p>) pada halaman.
* Kapan Menggunakannya: Ketika ingin **menerapkan gaya umum** pada semua element dengan **jenis tag tertentu**.
### 2. Selector Universal (Ex: "*"):
```
* {
  `Margin`: 0;
  `Padding`: 0;
}
```
* Kegunaan pada contoh: Selector universal digunakan untuk menghilangkan `Margin` dan `Padding` default pada semua element di halaman.
* Kapan Menggunakannya: Digunakan saat ingin mengatur beberapa gaya dasar **secara global** di seluruh halaman web.
### 3. Pseudo-Elements (Ex: `::before`, `::first-line`, etc):
```
blockquote::before {
  content: "\201C"; /* Menambahkan tanda kutip sebelum blok kutip */
}
```
* Kegunaan: Pseudo-element `::before` digunakan untuk menambahkan tanda kutip ("\201C") sebelum element blok kutip (<blockquote>).
* Kapan Menggunakannya: Digunakan ketika ingin menambahkan konten tambahan pada element yang dipilih **sesuai dengan kondisi yang diberikan pada pseudo-element**. Tiap pseudo-element memiliki kondisi dan kegunaanya masing-masing.
### 4. Pseudo-Classes(Ex `:hover`, `focus`, `:nth-child`, etc):
```
a:hover {
  color: red; /* Mengubah warna teks saat menghover tautan */
}
```
* Kegunaan: Pseudo-class `:hover` digunakan untuk mengubah warna teks saat tautan (`<a>`) dihover oleh mouse.
* Kapan Menggunakannya: Digunakan untuk memberikan interaksi tambahan pada element berdasarkan perilaku pengguna ataupun struktur dokumen HTML, seperti mengubah tampilan saat element dihover atau diklik. Tiap pseudo-classes memiliki kegunaanya masing-masing.
## HTML5 Tag
HTML5 adalah versi terbaru dari bahasa markup HTML yang memperkenalkan banyak element baru untuk meningkatkan semantik dan struktur dokumen web.

### 1. `<header>`
```
<header>
  <h1>Halaman Utama</h1>
  <p>Selamat datang di situs web kami.</p>
</header>
```
Digunakan untuk menggambarkan bagian atas dari sebuah element atau bagian dalam halaman web, seperti judul atau logo situs.

### 2. `<nav>`
```
<nav>
  <ul>
    <li><a href="#">Beranda</a></li>
    <li><a href="#">Tentang Kami</a></li>
    <li><a href="#">Layanan</a></li>
    <li><a href="#">Hubungi Kami</a></li>
  </ul>
</nav>
```
Digunakan untuk mengelompokkan tautan navigasi utama di dalam elemen, seperti menu navigasi situs.

### 3. `<main>`
```
<main>
  <h2>Artikel Terbaru</h2>
  <article>
    <h3>Judul Artikel 1</h3>
    <p>Isi artikel pertama.</p>
  </article>
  <article>
    <h3>Judul Artikel 2</h3>
    <p>Isi artikel kedua.</p>
  </article>
</main>
```
Digunakan untuk menggambarkan isi utama dari halaman web, dan biasanya hanya ada satu element `<main>` per halaman.

### 4. `<section>`
```
<section>
  <h2>Berita Terkini</h2>
  <article>
    <h3>Judul Berita 1</h3>
    <p>Isi berita pertama.</p>
  </article>
  <article>
    <h3>Judul Berita 2</h3>
    <p>Isi berita kedua.</p>
  </article>
</section>
```
Digunakan untuk mengelompokkan konten yang terkait dalam sebuah bagian, seperti artikel dalam sebuah berita.

### 5. `<aside>`
```
<aside>
  <h3>Artikel Terkait</h3>
  <ul>
    <li><a href="#">Artikel 1</a></li>
    <li><a href="#">Artikel 2</a></li>
    <li><a href="#">Artikel 3</a></li>
  </ul>
</aside>
```
Digunakan untuk menggambarkan konten yang sekunder atau tambahan dalam halaman, seperti sidebar.

### 6. `<footer>`
```
<footer>
  <p>&copy; 2023 Nama Situs. Hak Cipta Dilindungi.</p>
  <p><a href="#">Kebijakan Privasi</a> | <a href="#">Syarat & Ketentuan</a></p>
</footer>
```
Digunakan untuk menggambarkan bagian bawah dari sebuah element atau bagian dalam halaman web, seperti informasi hak cipta atau tautan ke halaman lain.

### 7. `<figure>` dan `<figcaption>`
```
<figure>
  <img src="gambar.jpg" alt="Deskripsi gambar">
  <figcaption>Gambar ilustrasi produk.</figcaption>
</figure>
```
`<figure>` digunakan untuk mengelompokkan element multimedia, seperti gambar atau video, bersama dengan element `<figcaption>` yang digunakan untuk memberikan keterangan atau deskripsi.

### 8. `<time>`
```
<p>Artikel ini diterbitkan pada <time datetime="2023-10-05">5 Oktober 2023</time>.</p>
```
Digunakan untuk menggambarkan waktu atau tanggal dalam format yang dapat dibaca oleh mesin, seperti tanggal publikasi artikel.

### 9. `<mark>`
```
<p>Deadline <mark>4 Oktober 2023</mark>.</p>
```
Digunakan untuk menyorot atau memberi penekanan pada teks tertentu dalam dokumen.

## `Margin` VS `Padding`
![google](https://media.geeksforgeeks.org/wp-content/uploads/20210317151556/marginpadding.png)

Ketika merancang tata letak halaman web dengan CSS, penting untuk memahami perbedaan antara `Margin` dan `Padding`. Kedua properti ini memengaruhi ruang di sekitar dan di dalam element HTML, dan mereka memiliki fungsi yang berbeda.

### `Margin`
`Margin` adalah ruang di luar element HTML. `Margin` mendefinisikan jarak antara element dan element lain di sekitarnya. `Margin` digunakan untuk mengendalikan jarak antara element dengan element lainnya.
Contoh:

```
.div1 {
  margin: 10px;
}

.div2 {
  margin: 20px 10px;
}
```

### `Padding`
`Padding` adalah ruang di dalam element HTML.
`Padding` mendifinisikan jarak antara konten element dan tepi element itu sendiri. `Padding` digunakan untuk mengendalikan jarak antara konten element dan batas element itu sendiri.
Contoh:

```
.div1 {
  `Padding`: 10px;
}

.div2 {
  `Padding`: 20px 10px;
}
```

Ringkasan
`Margin` memengaruhi ruang di luar elemen, sementara `Padding` memengaruhi ruang di dalam elemen.
`Margin` digunakan untuk mengatur jarak antara element dengan element lainnya, sedangkan `Padding` digunakan untuk mengatur jarak antara konten element dan tepi element itu sendiri.
Memahami perbedaan antara `Margin` dan `Padding` penting untuk mengontrol tata letak dan tampilan elemen-element dalam halaman web.

## `Tailwind` VS `Bootstrap`
Ketika memilih framework CSS untuk pengembangan web, ada beberapa perbedaan antara `Tailwind` CSS dan `Bootstrap` yang perlu dipertimbangkan, serta situasi di mana salah satu lebih sesuai daripada yang lain.

### `Tailwind` CSS

`Tailwind` CSS adalah framework CSS yang bersifat **utility-first**, artinya membangun tampilan dengan menggabungkan kelas-kelas utilitas ke element HTML. Ini memberikan tingkat fleksibilitas yang tinggi dalam menyesuaikan tampilan elemen.

Cocok digunakan ketika ingin **memiliki kontrol yang sangat detail** atas tampilan suatu element.
Baik untuk proyek-proyek yang memerlukan desain kustom dan tidak ingin diikat oleh gaya pra-didefinisikan.

```
<div class="bg-blue-500 p-4 rounded-lg">
  <p class="text-white">Ini adalah element dengan latar belakang biru dan padding.</p>
</div>
```

### `Bootstrap`

`Bootstrap` adalah framework CSS yang telah dirancang dengan gaya desain yang sudah ada dan komponen-komponen yang telah didefinisikan sebelumnya. Ini menyediakan komponen-komponen **siap pakai dan tata letak yang dapat digunakan dengan cepat**.

Cocok digunakan untuk pengembangan web yang cepat dan **tidak memerlukan desain kustom yang rumit**. Berguna untuk proyek-proyek yang ingin memanfaatkan komponen-komponen UI yang sudah ada.
```
<div class="container">
  <div class="alert alert-primary">
    <p>Ini adalah pesan peringatan dengan warna biru.</p>
  </div>
</div>
```
### Kesimpulan
* `Tailwind` CSS cocok digunakan ketika ingin desain yang sangat kustom dan fleksibilitas tinggi dalam mengontrol tampilan elemen.
* `Bootstrap` cocok digunakan ketika ingin pengembangan yang cepat dengan komponen-komponen UI yang sudah ada dan tampilan yang sudah didefinisikan sebelumnya.

## _Step-by-step_ pengerjaan tugas
### 1. Hal-Hal Umum yang Ditambahkan
Agar lebih rapih maka diaplikasikan hal-hal berikut,
#### Container
```
<div class="container">
    <!-- Konten -->
</div>
```
Pada kode di atas, class "container" digunakan untuk membuat kontainer dengan lebar terbatas yang akan mengatur kontennya secara otomatis di tengah halaman.

#### Row
```
<div class="row justify-content-center">
    <!-- Konten -->
</div>
```
Class "row" digunakan untuk membuat baris (row) yang berisi konten. Penggunaan class "justify-content-center" mengatur posisi konten di tengah horizontal.

#### Card
```
<div class="card mt-5">
    <!-- Konten -->
</div>
```
Kelas "card" digunakan untuk membuat tampilan kartu dengan bayangan dan bingkai.

#### Form Group
```
<div class="form-group">
    <!-- Konten formulir -->
</div>
```
Class "form-group" digunakan untuk mengelompokkan elemen-elemen formulir, seperti label dan input, sehingga dapat diatur dengan lebih baik.

#### Form Control
```
<input type="text" name="username" id="username" class="form-control" placeholder="Username">
```
Class "form-control" digunakan untuk mengubah tampilan elemen input agar memiliki gaya yang seragam dan responsif.

#### Tombol
```
<button class="btn btn-primary login_btn" type="submit">Login</button>
```
Kelas "btn" digunakan untuk membuat tombol dengan tampilan yang seragam, dan "btn-primary" memberikan warna latar belakang biru pada tombol.

#### Daftar Tanpa Gaya
```
<ul class="list-unstyled mt-3">
    <!-- Daftar -->
</ul>
```
Kelas "list-unstyled" digunakan untuk menghilangkan gaya bawaan daftar dan margin pada elemen daftar yang tidak terurut.

##### Teks Tengah
```
<p class="text-center mt-3">Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
```
Class "text-center" digunakan untuk mengatur teks menjadi tengah secara horizontal.

### 2. login.html
Selain hal umum yang digunakan, berikut tambahan aplikasi pada `login.html`:
#### Custom Internal CSS
```
<style>
    .text-danger {
        color: red;
    }
</style>
```
```
<li class="text-danger">{{ message }}</li>
```
Kelas "text-danger" digunakan untuk memberikan warna teks merah pada pesan error atau peringatan. CSS untuk kelas ini telah ditentukan dengan CSS internal.
#### Hasil Akhir
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card mt-5">
                <div class="card-body">
                    <h1 class="card-title text-center">Login</h1>
                    <form method="POST" action="">
                        {% csrf_token %}
                        <div class="form-group">
                            <label for="username">Username:</label>
                            <input type="text" name="username" id="username" class="form-control" placeholder="Username">
                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" name="password" id="password" class="form-control" placeholder="Password">
                        </div>
                        <div class="form-group text-center mt-3">
                            <button class="btn btn-primary login_btn" type="submit">Login</button>
                        </div>
                    </form>
                    <style>
                        .text-danger {
                            color: red;
                        }
                    </style>
                    {% if messages %}
                        <ul class="list-unstyled mt-3">
                            {% for message in messages %}
                                <li class="text-danger">{{ message }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                    <p class="text-center mt-3">Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock content %}
```
### 3. register.html
`register.html` hanya mengaplikasikan yand ada pada hal umum.
#### Hasil Akhir
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card mt-5 mb-4"> <!-- Added 'mb-4' class for margin -->
                <div class="card-body">
                    <h1 class="card-title text-center">Register</h1>
                    <form method="POST">
                        {% csrf_token %}
                        <table class="table">
                            {{ form.as_table }}
                        </table>
                        <div class="text-center mt-3">
                            <input type="submit" name="submit" value="Register" class="btn btn-primary"/>
                        </div>
                    </form>

                    {% if messages %}
                        <ul class="list-unstyled mt-3">
                            {% for message in messages %}
                                <li class="text-danger">{{ message }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>

{% endblock content %}
```
### 4. create_product.html
`create_product.html` hanya mengaplikasikan yand ada pada hal umum.
#### Hasil Akhir
```
{% extends 'base.html' %} 

{% block content %}
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card mt-5 mb-4"> <!-- Added 'mb-4' class for margin -->
                <div class="card-body">
                    <h1 class="card-title text-center">Add New Product</h1>
                    <form method="POST">
                        {% csrf_token %}
                        <table class="table">
                            {{ form.as_table }}
                            <tr>
                                <td></td>
                                <td>
                                    <input type="submit" value="Add Product" class="btn btn-primary btn-block"/> <!-- Added 'btn-block' class -->
                                </td>
                            </tr>
                        </table>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

### 5. main.html
Berikut hal lain yang diaplikasikan pada `main.html` yang tidak ada di bagian umum,

#### Container Full Width:
```
<div class="col-md-12">
    <!-- Konten -->
</div>
```
Dalam kode ini, kolom (column) mengisi lebar penuh halaman dengan class "col-md-12".

#### Custom Internal CSS:
Berikut adalah contoh CSS kustom pada element yang ingin ditunjuk yang ditambahkan dalam tag `<style>`:
```
<style>
    /* Mengatur tata letak dan margin elemen-elemen tertentu */
    .button-group {
        display: flex;
        justify-content: space-between;
        margin-top: 10px;
    }
    .product-card {
        margin-bottom: 20px;
    }
    /* Mengatur fleksibilitas tombol */
    .button-group .btn {
        flex: 1;
    }
    /* Menjadikan tombol "-" dan "+" bersebelahan */
    .button-group .btn-group {
        display: flex;
        align-items: center;
    }
    .button-group .btn-group .btn {
        flex: none;
    }
</style>
```
#### Custom Inline CSS:
Inline CSS digunakan ketika terjadi kasus-kasus khusus dan bukan keumuman seperti pada Internal CSS, berikut contohnya,
```
<div style="max-height: 500px; overflow-y: scroll;">
    <!-- Replace the table with a card -->
    ...
<div>
```
#### Card untuk Produk:
```
<!-- Menggantikan tabel dengan card untuk menampilkan data produk -->
<div class="card">
    <div class="card-body">
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
        <div class="row">
            {% for product in products %}
                <div class="col-md-4 product-card">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">{{ product.name }}</h5>
                            <p class="card-text">
                                Amount: {{ product.amount }}<br>
                                Description: {{ product.description }}<br>
                                Price: {{ product.price }}<br>
                                Date Added: {{ product.date_added }}
                            </p>
                        </div>
                        <div class="card-footer">
                            <div class="button-group">
                                <form method="post" action="{% url 'main:decrement_amount' product.id %}">
                                    {% csrf_token %}
                                    <div class="btn-group">
                                        <button type="submit" class="btn btn-primary btn-sm">-</button>
                                        <button type="submit" class="btn btn-primary btn-sm">+</button>
                                    </div>
                                </form>
                                <form method="post" action="{% url 'main:delete_product' product.id %}">
                                    {% csrf_token %}
                                    <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</div>
```
Kode ini menggunakan elemen "card" untuk menampilkan informasi produk, yang lebih cocok daripada tabel dalam konteks ini. Setiap produk ditampilkan dalam "card" terpisah.

#### Tombol "Add New Product" dan "Logout":
```
<!-- Tombol "Add New Product" dengan class "btn btn-primary" -->
<a href="{% url 'main:create_product' %}">
    <button class="btn btn-primary">Add New Product</button>
</a>

<!-- Tombol "Logout" dengan class "btn btn-danger" -->
<a href="{% url 'main:logout' %}">
    <button class="btn btn-danger">Logout</button>
</a>
```
Tombol-tombol ini juga menggunakan kelas Bootstrap "btn" untuk tampilan yang seragam. Tombol "Add New Product" memiliki warna biru (btn-primary), sementara tombol "Logout" memiliki warna merah (btn-danger).

#### Hasil Akhir
{% extends 'base.html' %}

{% block content %}
<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-12"> <!-- Changed 'col-md-6' to 'col-md-12' for full width -->
            <div class="card mt-4 mb-4">
                <div class="card-body">
                    <h1 class="card-title text-center">Albion Storage</h1>
                    <h4><strong>AccountID: </strong>{{ accountID }}</h4>
                    <p><strong>Balance: </strong>{{ balance }}</p>
                    <h4><strong>Inventory</strong></h4>
                    
                    <p>Kamu menyimpan {{ product_count }} item pada inventory</p>  <!-- Display the product count -->

                    <style>
                        /* Custom CSS for margin and layout */
                        .button-group {
                            display: flex;
                            justify-content: space-between;
                            margin-top: 10px;
                        }
                        /* Custom CSS for the product card grid */
                        .product-card {
                            margin-bottom: 20px;
                        }
                        /* Custom CSS for flexible buttons */
                        .button-group .btn {
                            flex: 1;
                        }
                        /* Custom CSS to make "-" and "+" buttons side by side */
                        .button-group .btn-group {
                            display: flex;
                            align-items: center;
                        }
                        .button-group .btn-group .btn {
                            flex: none;
                        }
                    </style>
                    
                    <div style="max-height: 500px; overflow-y: scroll;">
                        <!-- Replace the table with a card -->
                        <div class="card">
                            <div class="card-body">
                                {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
                                <div class="row">
                                    {% for product in products %}
                                        <div class="col-md-4 product-card">
                                            <div class="card">
                                                <div class="card-body">
                                                    <h5 class="card-title">{{ product.name }}</h5>
                                                    <p class="card-text">
                                                        Amount: {{ product.amount }}<br>
                                                        Description: {{ product.description }}<br>
                                                        Price: {{ product.price }}<br>
                                                        Date Added: {{ product.date_added }}
                                                    </p>
                                                </div>
                                                <div class="card-footer">
                                                    <div class="button-group">
                                                        <form method="post" action="{% url 'main:decrement_amount' product.id %}">
                                                            {% csrf_token %}
                                                            <div class="btn-group">
                                                                <button type="submit" class="btn btn-primary btn-sm">-</button>
                                                                <button type="submit" class="btn btn-primary btn-sm">+</button>
                                                            </div>
                                                        </form>
                                                        <form method="post" action="{% url 'main:delete_product' product.id %}">
                                                            {% csrf_token %}
                                                            <button type="submit" class="btn btn-danger btn-sm">Delete</button>
                                                        </form>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    {% endfor %}
                                </div>
                            </div>
                        </div>
                        <!-- End of card -->
                    </div>                                                           

                    <br />
                    <h5>Sesi terakhir login: {{ last_login }}</h5>
                    <div class="d-flex justify-content-between">
                        <a href="{% url 'main:create_product' %}">
                            <button class="btn btn-primary">Add New Product</button>
                        </a>
                        <a href="{% url 'main:logout' %}">
                            <button class="btn btn-danger">Logout</button>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div style="text-align: right;">
            <p><strong>Name:</strong> {{ name }} &nbsp;&nbsp;&nbsp;&nbsp; <strong>Class:</strong> {{ class }}</p>
        </div>
    </div>
</div>
{% endblock content %}