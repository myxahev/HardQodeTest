from rest_framework.decorators import api_view
from rest_framework.response import Response
from src.education.models import Product
from src.rest.serializers import ProductSerializer


@api_view(['GET'])
def product_list_api(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
