from django.contrib import admin
from . models import ProductImage,ProductCategories,Products,Customer,Order
from .forms import ProductsForm
# Register your models here.

class ShopAdminArea(admin.AdminSite):
    site_header='Ecommerce App'

class ProductImageAdmin(admin.ModelAdmin):
    fields = ('image_tag', 'path',)
    list_display = ['image_tag',]
    readonly_fields = ['image_tag']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','description','price','category','stock','status']
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','status']
    exclude = ['password']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone','state','zip','address1','status']
    readonly_fields = ['provider_order_id','payment_id','signature_id','ordered_date']




shop_site = ShopAdminArea(name='ShopAdmin')


shop_site.register(ProductImage,ProductImageAdmin)
shop_site.register(ProductCategories)
shop_site.register(Customer, CustomerAdmin)
shop_site.register(Order, OrderAdmin)


shop_site.register(Products, ProductsAdmin)
