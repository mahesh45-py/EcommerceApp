from django.urls import path
from . import views

urlpatterns = [
    # path('', include('shoppingCart.urls')),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('careers', views.careers, name='careers'),
    path('cart', views.cart, name='cart'),
    path('product/<int:product_id>', views.product, name='product'),
    path('customer', views.customer, name='customer'),
    path('order', views.order, name='order'),
]