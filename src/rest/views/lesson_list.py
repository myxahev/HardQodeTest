from rest_framework.decorators import api_view
from rest_framework.response import Response

from src.education.models import Lesson
from src.authentication.models import UserProductAccess
from src.rest.serializers import LessonSerializer


@api_view(['GET'])
def lesson_list_by_product_api(request, product_id):
    if request.method == 'GET':
        lessons = Lesson.objects.filter(product_id=product_id)
        if request.user.is_authenticated:
            user_accesses = UserProductAccess.objects.filter(user=request.user, product_id=product_id).exists()
            if user_accesses:
                lessons = lessons.all()
            else:
                return Response({'message': 'У вас нет доступа к этому продукту'}, status=403)
        else:
            return Response({'message': 'Требуется аутентификация'}, status=401)

        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)
