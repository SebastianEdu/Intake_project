from django.shortcuts import render
from.models import Brand, Car
from django.views import generic

# Create your views here.
def index(request):
	brands_available=Brand.objects.all().count()
	cars_available=Car.objects.all().count()

	return render(
        request,
        'index.html',
        context={'brands_available':brands_available,'cars_available':cars_available},
    )

class CarListView(generic.ListView):
	model = Car

class CarDetailView(generic.DetailView):
	model = Car

class BrandListView(generic.ListView):
	model = Brand

class BrandDetailView(generic.DetailView):
	model = Brand

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car

class CarCreate(CreateView):
	model = Car
	fields = '__all__'
	#initial = {'car_model':'',}

class CarUpdate(UpdateView):
	model = Car
	fields = '__all__'

class CarDelete(DeleteView):
	model = Car
	success_url = reverse_lazy('cars')

from django.contrib.auth.forms import UserCreationForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
