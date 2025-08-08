from django.urls import path
from .views import ModelListView, ModelContextView

urlpatterns = [
    path('models/', ModelListView.as_view(), name='model-list'),
    path('models/<str:model_name>/context/', ModelContextView.as_view(), name='model-context'),
]
