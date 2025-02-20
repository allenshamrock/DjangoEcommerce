from django.shortcuts import render,get_object_or_404,redirect
from Products.models import Product,Variation
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import CartItem,Cart
# Create your views here.

def _cart_id(request):
    """
    Get or create cart id from the session
    """
    if not request.session.session_key:
        request.session.create()
    
    cart_id = request.session.session_key
    return cart_id


def add_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    product_variation = []

    # Extract variation from post data
    if request.method == 'POST':
        for key,value in request.POST.items():
            try:
                variation = Variation.objects.get(
                    product=product,
                    variation_category__iexact =key,
                    variation_value__iexact = value
                )
                product_variation.append(variation)
            except Variation.DoesNotExist:
                pass
    # Determine cart ownership
    if request.user.is_authenticated:
        user = request.user
        cart = None
    else:
        cart_id = _cart_id(request)
        user = None
        cart, created = Cart.objects.get_or_create(cart_id=cart_id)

    # Check if the cart item already exists
    cart_items = CartItem.objects.filter(
        product=product,
        user=user,
        cart=cart
    )

    existing_variation_list = []
    id_list = []

    for item in cart_items:
        existing_variation = list(item.variations.all())
        existing_variation_list.append(existing_variation)
        id_list.append(item.id)

    if product_variation in existing_variation_list:
        # Increase the cart item quantity
        index = existing_variation_list.index(product_variation)
        item_id = id_list[index]
        item = CartItem.objects.get(id=item_id)
        item.quantity += 1
        item.save()
    else:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            user=user
        )
        if product_variation:
            cart_item.variation.add(*product_variation)
            cart_item.save()

    messages.success(request, "The product has been added successfully to the cart")
    return redirect("cart")