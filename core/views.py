from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .registry import ModelRegistry
from .context import ModelContextGenerator
from .serializers import ModelListSerializer, ModelContextSerializer

def root_view(request):
    return HttpResponse('Welcome to SmartMCP - Model Context Protocol API System')

class ModelListView(APIView):
    def get(self, request):
        models = ModelRegistry.get_all_models()
        serializer = ModelListSerializer(models.values(), many=True)
        return Response(serializer.data)

class ModelContextView(APIView):
    def get(self, request, model_name):
        models = ModelRegistry.get_all_models()
        if model_name not in models:
            return Response({'error': 'Model not found'}, status=404)
        model = models[model_name]['model']
        context = ModelContextGenerator.get_model_context(model)
        serializer = ModelContextSerializer(context)
        return Response(serializer.data)
