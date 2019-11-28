from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Car(models.Model):

	car_brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True)
	car_model = models.CharField(max_length=50, help_text="Ingrese el modelo del auto")
	car_plate = models.IntegerField( primary_key=True, blank=False,default='111111')
	car_price = models.IntegerField(help_text='Ingrese precio estimado de venta')
	car_category = models.CharField(max_length=30,default='---', help_text='Ingrese la categoria/disciplina del vehiculo')
	car_year = models.IntegerField( help_text='Ingrese el año del auto')
	car_engine = models.CharField(max_length=30, default='---', help_text='Ingrese el tipo de motor del vehiculo')
	car_cilindrada = models.FloatField( help_text='Ingrese la cilindrada del motor')

	DriveTrain_STATUS = (
		('4WD', '/Four Wheel Drive / Traccion Integral'),
		('AWD', 'All Wheel Drive / Traccion Total'),
		('FWD', 'Front Wheel Drive / Traccion Delantera'),
		('RWD', 'Rear Whell Drive / Traccion Trasera'),
	)

	car_drivetrain = models.CharField(
		max_length=3, 
		choices=DriveTrain_STATUS,
		blank=False,
		default='---3', 
		help_text='Ingrese la opcion de traccion que posea el vehiculo')

	def __str__(self):
		return self.car_model

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('car-detail', args=[str(self.car_plate)])



class Brand(models.Model):
	brand_name = models.CharField(max_length=40) 


	class Meta:
		ordering = ['brand_name']

	def get_absolute_url(self):
		return reverse('brand-detail', args=[str(self.id)])

	def __str__(self):
		return self.brand_name