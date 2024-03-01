from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_models(self):
        for model in apps.get_models():
            if model._meta.app_label != 'django.contrib.auth':
                with self.subTest(model=model):
                    instance = model.objects.create()
                    self.assertIsNotNone(instance)
                    