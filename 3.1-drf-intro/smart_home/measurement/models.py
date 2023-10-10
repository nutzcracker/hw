from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
	name = models.CharField(max_length=20, verbose_name='Название')
	description = models.CharField(max_length=50, verbose_name='Описание')

	def __str__(self):
		return self.name


class Measurement(models.Model):
	temp = models.FloatField(verbose_name='температура')
	created_at = models.DateTimeField(auto_now=True)
	id_sens = models.IntegerField(default=1, verbose_name='номер датчика')
