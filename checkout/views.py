from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    emplate = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M6tzPBsS8bnWf1zeIpLCLVFziZoJ19WtkQez8TIyXVwswQfnBiO62f8DKjQxXBm4MnTfka4RFxwhytbPTRCEeQe00OZFYU9Ux',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)