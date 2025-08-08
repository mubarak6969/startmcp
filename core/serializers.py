from rest_framework import serializers
from .registry import ModelRegistry
from .context import ModelContextGenerator

class ModelContextSerializer(serializers.Serializer):
    model_name = serializers.CharField()
    fields = serializers.ListField(child=serializers.DictField())

class ModelListSerializer(serializers.Serializer):
    name = serializers.CharField(source='model.__name__')
    permissions = serializers.DictField()
