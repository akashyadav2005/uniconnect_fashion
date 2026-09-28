from django import template

# Yeh line Django ko batati hai ki hum custom tags register kar rahe hain
register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    # Session se jo cart aati hai usme keys hamesha string format mein hoti hain
    # Isliye hum product.id ko string mein convert karke match karte hain
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(product, cart):
    # Product ki total price nikalne ke liye price ko quantity se multiply karte hain
    return product.price * cart_quantity(product, cart)

@register.filter(name='multiply')
def multiply(quantity, price):
    # Order history mein simple math ke liye
    return quantity * price