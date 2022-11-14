
from django.http import JsonResponse
from ..models import Order,Customer,Products
import requests
import json
from main.settings import CF_SECRET,CF_APP_ID,CF_ENDPOINT,BASE_URL
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

class OrdersService:
    def __init__(self):
        self.utilities = None
    
    def new_order(self,payload):
        try:
            value = 0
            products = payload.get('products')
            product_ids=[]
            for product in products:
                product_ids.append(product.get('id'))
                value+= int(product.get('price'))
            customer = payload.get('customer')
            ordered_customer = Customer.objects.filter(id=customer.get('id'))[0]
            order = Order(value=value,
                        first_name=payload.get('first_name'),
                        last_name=payload.get('last_name'),
                        email=payload.get('email'),
                        phone=payload.get('phone'),
                        country=payload.get('country'),
                        state=payload.get('state'),
                        zip=payload.get('zip'),
                        address1=payload.get('address1'),
                        address2=payload.get('address2'),
                        user=ordered_customer
                        )
            order.save()
            for pid in product_ids:
                product = Products.objects.filter(id=pid)[0]
                order.products.add(product)
            order.save()
            
            return_url=BASE_URL+'/?order_id={order_id}'
            url = CF_ENDPOINT+'/orders'
            paymentdata = {
                "order_id": 'order_'+str(order.pk),
                "order_amount":value,
                "order_currency":"INR",
                "customer_details":{
                    "customer_id": 'customer_'+str(customer.get('id')),
                    "customer_email":customer.get('email'),
                    "customer_phone":customer.get('phone'),
                    "customer_name":customer.get('first_name'),
                    },
                "order_meta":{
                    "return_url": return_url
                }
            }
            
            headers = {
                "accept": "application/json",
                "x-client-id": CF_APP_ID,
                "x-client-secret": CF_SECRET,
                "x-api-version": "2022-01-01",
                "content-type": "application/json"
            }
            
            resp = requests.post( url, json=paymentdata, headers=headers)
            response = json.loads(resp.text)
            order.provider_order_id = response.get('cf_order_id')
            order.signature_id = response.get('order_token')
            order.save()
            paymentUrl = response.get('payment_link')
            
            
            
            return JsonResponse({
                'status':True,
                'message':'ordered successful',
                'data': {
                    'paymentUrl':paymentUrl
                }
            })
        except Exception as err:
            print("OrdersService -> new_order -> "+str(err))
            return JsonResponse({
                'status':False,
                'message':'An Error Occured while creating account',
                'devMsg':str(err)
            })

    def update_order(self,payload):
        try:
            order_id = payload.get('order_id').split('_')[1]
            
            order = Order.objects.filter(id=order_id)[0]
            
            url = CF_ENDPOINT+"/orders/"+payload.get('order_id')+"/payments"

            headers = {
                "accept": "application/json",
                "x-client-id": CF_APP_ID,
                "x-client-secret": CF_SECRET,
                "x-api-version": "2022-01-01"
            }

            resp = requests.get(url, headers=headers)
            response = json.loads(resp.text)
            
            payment_id = response[0].get('cf_payment_id')
            payment_status = response[0].get('payment_status')
            order.payment_id = payment_id
            order.status = 'PS' if (payment_status == 'SUCCESS') else 'PF'
            order.save()

            if(payment_status == 'SUCCESS'):
                
                products = Order.objects.raw("select * from shop_order_products as sop left join shop_products as sp on sp.id=sop.products_id where order_id="+str(order.id))
                for productObj in products:
                    product = Products.objects.filter(id=productObj.products_id)[0]
                    prevQty = product.stock
                    product.stock = prevQty -1
                    product.save()
                
                data = {
                    'customer_name':order.first_name+' '+order.last_name,
                    'customer_phone':order.phone,
                    'order_id':order.id,
                    'order_date':order.ordered_date,
                    'order_value':order.value,
                    'products':products
                }
                msg_html = render_to_string('invoice.html',{'data':data})

                send_mail(subject='Thankyou for ordering in Ecommerce App.',message='Invoice',html_message=msg_html,from_email=settings.EMAIL_HOST_USER,recipient_list=[order.email])
                return JsonResponse({
                    'status':True,
                    'message':'Order placed successfully, Please check you email for more information',
                    'data': None
                })
            else:
                return JsonResponse({
                    'status':False,
                    'message':'Unable to place the order',
                    'devMsg': 'PG Status : '+payment_status
                })

        except Exception as err:
            print("OrdersService -> new_order -> "+str(err))
            return JsonResponse({
                'status':False,
                'message':'An Error Occured validating payment',
                'devMsg':str(err)
            })