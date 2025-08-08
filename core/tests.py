from django.test import TestCase
from .registry import ModelRegistry
from .models import Student
from .context import ModelContextGenerator

class ModelRegistryTests(TestCase):
    def test_model_registration(self):
        models = ModelRegistry.get_all_models()
        self.assertIn('Student', models)
        self.assertEqual(models['Student']['model'], Student)
        self.assertEqual(models['Student']['permissions'], {'can_view': ['admin'], 'can_edit': ['admin']})

    def test_model_context_generator(self):
        context = ModelContextGenerator.get_model_context(Student)
        self.assertEqual(context['model_name'], 'Student')
        self.assertEqual(len(context['fields']), 4)  # id, name, age, grade
        name_field = context['fields'][1]
        self.assertEqual(name_field['name'], 'name')
        self.assertEqual(name_field['type'], 'CharField')
        self.assertEqual(name_field['max_length'], 100)
        self.assertFalse(name_field['nullable'])
