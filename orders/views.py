from django.conf import settings
from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, user=request.user)
        if form.is_valid():
            order = form.save()
            if request.user.is_authenticated:
                user = request.user
                user.first_name = order.first_name
                user.last_name = order.last_name
                user.address = order.address
                user.save()
                order.user = user
                order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'order/created.html', {'order': order, 'key': settings.STRIPE_PUBLISHABLE_KEY})
    else:
        form = OrderCreateForm(user=request.user)
    return render(request, 'order/create.html', {'form': form})


def charge(request, order_id):
    order = Order.objects.filter(id=order_id).first()
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=int(order.get_total_price_for_order()),
            currency='usd',
            description='Parusa charge',
            source=request.POST['stripeToken']
        )
        order.paid = True
        order.save()

        return render(request, 'order/charge.html', {'order': order})
