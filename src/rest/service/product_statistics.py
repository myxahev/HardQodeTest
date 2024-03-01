from typing import List

from django.db.models import Count, F
from django.contrib.auth.models import User

from src.education.enums.product_stat import ProductStat
from src.authentication.models import Group, UserProductAccess
from src.education.models import Product


def calculate_product_statistics() -> List[ProductStat]:
    products = Product.objects.all()
    product_stats: List[ProductStat] = []

    for product in products:
        num_students = UserProductAccess.objects.filter(product=product).count()
        avg_group_fill = Group.objects.filter(product=product).annotate(
            num_students=Count('students')
        ).aggregate(
            avg_fill=Count('id', filter=F('num_students') > 0) * 100.0 / Count('id')
        )['avg_fill']

        total_users = User.objects.count()
        access_percentage = (num_students / total_users) * 100 if total_users != 0 else 0

        product_stat = ProductStat(
            id=product.id,
            name=product.name,
            num_students=num_students,
            avg_group_fill=avg_group_fill,
            access_percentage=access_percentage
        )
        product_stats.append(product_stat)

    return product_stats
