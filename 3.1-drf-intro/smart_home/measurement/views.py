# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView




class TempView(ListCreateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer

	def post(self, request):
		serializer = SensorSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response({'post': serializer.data})


class TView(RetrieveUpdateAPIView):
	queryset = Sensor.objects.all()
	serializer_class = SensorSerializer


class MeasurementView(ListCreateAPIView):
	queryset = Measurement.objects.all()
	serializer_class = MeasurementSerializer

	def post(self, request):
		serializer = MeasurementSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response({'post': serializer.data})