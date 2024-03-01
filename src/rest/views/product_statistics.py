from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.rest.service.product_statistics import calculate_product_statistics


@api_view(['GET'])
def product_statistics_api(request):
    if request.method == 'GET':
        product_stats = calculate_product_statistics()
        return Response(product_stats)
