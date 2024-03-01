import time
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from src.education.models import Product


def grant_access_to_product(request, product_id, user_id):
    product = get_object_or_404(Product, id=product_id)

    if product.start_datetime <= time.timezone.now():
        group = distribute_user_to_group(product)
        group.students.add(user_id)
        group.save()
        return JsonResponse({'message': 'Access granted and user distributed to group successfully.'})
    else:
        redistribute_groups(product)
        return JsonResponse({'message': 'Product has not started yet, redistributing groups.'})
