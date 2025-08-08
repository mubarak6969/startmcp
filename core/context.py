from django.apps import apps
from django.db.models import Field

class ModelContextGenerator:
    @staticmethod
    def get_model_context(model):
        fields = []
        for field in model._meta.get_fields():
            if isinstance(field, Field):
                fields.append({
                    'name': field.name,
                    'type': field.get_internal_type(),
                    'max_length': getattr(field, 'max_length', None),
                    'nullable': field.null,
                })
        return {
            'model_name': model.__name__,
            'fields': fields,
        }
