from django.db import models
from django.utils.html import escape
from main.settings import MEDIA_URL
from django.utils.html import mark_safe
# Create your models here.

status_options = (
        ('AC','Active'),
        ('NA','Not Active')
    )

class ProductCategories(models.Model):
    
    name=models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=2, default='AC', choices=status_options)

    def __str__(self) -> str:
        return self.name


class ProductImage(models.Model):
    path= models.ImageField(null=True, blank=True)
    def image_tag(self):
        
        return  mark_safe('<img src="%s" />' % escape(MEDIA_URL+str(self.path))) if self.path else ''
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True  
    def __str__(self) -> str:
        return str(self.path)


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(ProductCategories,on_delete=models.CASCADE)
    stock = models.IntegerField()
    status = models.CharField(max_length=2, default='AC', choices=status_options)
    images = models.ManyToManyField(ProductImage)
    def __str__(self) -> str:
        
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=16)
    status = models.CharField(max_length=2, default='AC', choices=(('AC','Active'),('BL','Blocked')))

    def __str__(self) -> str:
        
        return self.first_name



class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    value = models.IntegerField()
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    zip = models.CharField(max_length=7)
    address1 = models.TextField()
    address2 = models.TextField()
    status = models.CharField(max_length=2, default='PN', choices=(('IP','In Progress'),('PS','Payment Success'),('PF','Payment Failed'),('PN','Payment Pending'),('TS','Transit'),('DL','Delevered')))
    provider_order_id = models.CharField(max_length=40)
    payment_id = models.CharField(max_length=36)
    signature_id = models.CharField(max_length=128)
    ordered_date = models.DateTimeField(auto_now_add=True, blank=True)




    


    
