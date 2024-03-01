from rest_framework import serializers
from src.education.models import Product


class ProductSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'creator', 'name', 'start_datetime', 'cost', 'min_group_size', 'max_group_size', 'num_lessons']

    def get_num_lessons(self, obj):
        return obj.lessons.count()
