from django.test import TestCase
from .registry import ModelRegistry
from .models import Student

class ModelRegistryTests(TestCase):
    def test_model_registration(self):
        models = ModelRegistry.get_all_models()
        self.assertIn('Student', models)
        self.assertEqual(models['Student']['model'], Student)
        self.assertEqual(models['Student']['permissions'], {'can_view': ['admin'], 'can_edit': ['admin']})
