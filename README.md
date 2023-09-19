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
- Struktur: Data dalam XML dikelompokkan dalam elemen, dan setiap elemen memiliki tag pembuka dan penutup. Memungkinkan pendifinisian data yang terstruktur dan fleksibel. co:
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
- Penggunaan: Bahasa markup yang digunakan untuk mengatur tampilan dan struktur elemen-elemen web di browser.
- Struktur: HTML memiliki struktur yang ditentukan dengan baik, terdiri dari elemen-elemen seperti `<html>`, `<head>`, `<body>`, `<p>`, `<div>`, dan banyak lagi. Ini tidak digunakan untuk pertukaran data dalam format yang kaya, tetapi untuk menampilkan konten di browser. co:
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

3. **Mendukung Struktur Nested Array**: JSON mendukung struktur nested array, yang memungkinkan Anda untuk menyimpan data yang kompleks dengan mudah.

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
