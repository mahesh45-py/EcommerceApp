from django.shortcuts import render
from django.http import HttpResponse
from .services.products_services import ProductServices
import json
from django.views.decorators.csrf import csrf_exempt
from .services.customers_service import CustomersServices
from .services.orders_service import OrdersService
# Create your views here.

def home(request):
    
    products = ProductServices().getAllProducts()
    productsData = {
        'products':products,
        'title':'Homepage'
    }
    return render(request,'home.html',productsData)
def about(request):
    data = {
        'title':'About Us'
    }
    return render(request,'about.html',data)
def careers(request):
    data = {
        'title':'Careers'
    }
    return render(request,'careers.html',data)
def cart(request):
    data = {
        'title':'Cart'
    }
    return render(request,'cart.html',data)

def product(request, product_id):
    products = ProductServices().getAllProducts(product_id)
    productsData = {
        'product':products[0] if products else None,
        'title': products[0].name if products else '404'
    }
    
    return render(request,'product.html',productsData)

@csrf_exempt
def customer(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        return CustomersServices().register_user(data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        return CustomersServices().validate_user(data)

@csrf_exempt
def order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return OrdersService().new_order(data)
    if request.method == 'PUT':
        data = json.loads(request.body)
        return OrdersService().update_order(data)