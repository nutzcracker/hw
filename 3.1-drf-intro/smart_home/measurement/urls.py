from django.urls import path
from .views import TempView, TView, MeasurementView

urlpatterns = [
    path('sensors/', TempView.as_view()),
    path('sensors/<pk>/', TView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    
]
