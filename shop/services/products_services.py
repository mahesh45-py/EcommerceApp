from ..models import Products,ProductImage
from django.db import connection


class ProductServices:
    def __init__(self):
        self.utilites = None

    def getAllProducts(self,id=None):
        try:
            if id:
                products =  Products.objects.filter(id=id).filter(status='AC')
            else:
                products = Products.objects.filter(status='AC')
            
            data = []
            for product in products:
                p_id = product.id
                product.photos = [i for i in ProductImage.objects.raw("select * from shop_products_images where products_id="+str(p_id))]
                data.append(product)

            return data


        except Exception as err:
            print("ProductServices -> getAllProducts -> "+str(err))
            return None