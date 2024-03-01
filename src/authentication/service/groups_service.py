from src.authentication.models import Group


def distribute_user_to_group(product):
    group = None
    groups = product.groups.all().order_by('students__count')

    for grp in groups:
        if grp.students.count() < product.max_group_size:
            group = grp
            break

    if not group:
        group = Group.objects.create(product=product, name=f'Group {product.groups.count() + 1}')

    return group


def redistribute_groups(product):
    groups = product.groups.all()
    total_students = sum([group.students.count() for group in groups])
    average_students = total_students // groups.count()
    remaining_students = total_students % groups.count()

    for group in groups:
        if remaining_students > 0:
            max_students = average_students + 1
            remaining_students -= 1
        else:
            max_students = average_students

        group.max_group_size = max_students
        group.save()
