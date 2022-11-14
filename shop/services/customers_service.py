from django.http import JsonResponse
from ..models import ProductCategories, Customer

class CustomersServices:
    def __init__(self):
        self.utilites = None
 
    def validate_user(self,payload):
        try:
            existing = Customer.objects.filter(email=payload.get('email'),password=payload.get("password")).values()
            if not existing:
                return JsonResponse({
                'status':False,
                'message':'Invalid Credentials, Please try again'
            })
            customer = existing[0]
            if customer.get('status')!='AC':
                return JsonResponse({
                'status':False,
                'message':'Your Account has been suspended, please contact support team!'
                
            })
            del customer['password']
            return JsonResponse({
                'status':True,
                'message':'Login Successful, Please continue to order',
                'data':customer
            })
        except Exception as err:
            print("CustomersServices -> validate_user -> "+str(err))
            return JsonResponse({
                'status':False,
                'message':'An Error Occured while creating account',
                'devMsg':str(err)
            })

    def register_user(self,payload):
        try:
            existing = Customer.objects.filter(email=payload.get('email'))
            if existing:
                return JsonResponse({
                'status':False,
                'message':'Email Already Exist, please login to continue'
            })
            new_customer = Customer(first_name=payload.get('first_name'),last_name=payload.get('last_name'),email=payload.get('email'),phone=payload.get('phone'),password=payload.get('password'))
            new_customer.save()
            return JsonResponse({
                'status':True,
                'message':'Account Created Successfully, please login to continue'
            })
        except Exception as err:
            print("CustomersServices -> register_user -> "+str(err))
            return JsonResponse({
                'status':False,
                'message':'An Error Occured while creating account',
                'devMsg':str(err)
            })



    