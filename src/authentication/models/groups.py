from django.db import models
from django.contrib.auth.models import User
from src.education.models import Product


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, related_name='groups')

    def __str__(self):
        return self.name
