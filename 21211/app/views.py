from .models import Order, OrderItem
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404
from decimal import Decimal, ROUND_DOWN
def checkout(request, order_pk):

    #Method 1
    try:
        order = Order.objects.get(pk = order_pk)
        order_items = OrderItem.objects.filter(order = order)
    except Order.DoesNotExist:
        raise Http404
    

    #Method 2
    """
    try:
        order = Order.objects.get(pk = order_pk)
        order_items = OrderItem.objects.filter(order = order)
    except Order.DoesNotExist:
        return HttpResponse(status = 404)
    """

    #Method 3
    """
    order = get_object_or_404(Order,pk = order_pk)
    order_items = OrderItem.objects.filter(order = order)
    """
    
    total_price = Decimal('0.00')
    for item in order_items:
        total_price += Decimal(item.product.price) * item.quantity
    total_price = total_price.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
    return JsonResponse({'total_price': str(total_price)})



