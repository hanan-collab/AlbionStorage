import json
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Sum, F
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    user = request.user
    products = Product.objects.filter(user=request.user)
    product_count = products.count()
    # Calculate the balance by summing up the product of 'amount' and 'item_price' for all products
    balance = products.aggregate(balance=Sum(F('amount') * F('price')))['balance']
    if balance is None:
        balance = 0
    context = {
        'name' : 'Hanan Adipratama',
        'class' : 'PBP B',
        'accountID': request.user.username,
        'products' : products,
        'product_count': product_count,
        'balance' : balance,
        'last_login': request.COOKIES['last_login'],

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

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
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def decrement_amount(request, id):
    data = get_object_or_404(Product, pk=id)
    if data.amount > 0:
        data.amount -= 1
        data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def increment_amount(request, id):
    data = get_object_or_404(Product, pk=id)
    data.amount += 1
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def delete_product(request, id):
    data = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        data.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_product_json(request):
    user = request.user
    product_item = Product.objects.filter(user=user)
    return HttpResponse(serializers.serialize('json', product_item))

def get_balance(request):
    user = request.user
    products = Product.objects.filter(user=user)
    balance = products.aggregate(balance=Sum(F('amount') * F('price')))['balance']
    return HttpResponse(balance)

def get_product_count(request):
    user = request.user
    products = Product.objects.filter(user=user)
    product_count = products.count()
    return HttpResponse(product_count)

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        price = request.POST.get("price")
        user = request.user

        new_product = Product(name=name, amount=amount, description=description, price=price, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            amount = 0,
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)