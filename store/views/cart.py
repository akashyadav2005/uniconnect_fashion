from django.shortcuts import render
from django.views import View
from store.models.products import Products

class Cart(View):
    def get(self, request):
        # Session se cart nikalna
        cart = request.session.get('cart')
        
        # Agar cart exist nahi karta ya khali hai, toh empty dictionary set karein
        if not cart:
            request.session['cart'] = {}
            cart = request.session['cart']
            
        # Cart ki keys (jo ki product IDs hain) ko ek list mein convert karna
        ids = list(cart.keys())
        
        # Database se un IDs wale products ko fetch karna
        products = Products.get_products_by_id(ids)
        
        # Products ko template mein bhej dena
        return render(request, 'cart.html', {'products': products})