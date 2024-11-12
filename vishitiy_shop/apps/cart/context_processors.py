from cart.cart import Cart


def cart(request):
    """Creating context processor for cart to be available in all templates"""
    return {"cart": Cart(request)}
