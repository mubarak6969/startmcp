from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        from .models import Student
        from .registry import ModelRegistry
        ModelRegistry.register(Student, permissions={'can_view': ['admin'], 'can_edit': ['admin']})
