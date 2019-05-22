from cart.cart import Cart
from products.models import Category


def cart(request):
    return {'cart': Cart(request), 'categories': Category.objects.all()}
