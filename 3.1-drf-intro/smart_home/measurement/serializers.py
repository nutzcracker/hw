from rest_framework import serializers
from .models import Sensor, Measurement

class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = ['id', 'name', 'description']

	def create(self, validated_data):

		return Sensor.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.description = validated_data.get("description", instance.description)
		instance.save()

		return instance


class MeasurementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Measurement
		fields = ['id_sens', 'temp']

	def create(self, validated_data):

		return Measurement.objects.create(**validated_data)