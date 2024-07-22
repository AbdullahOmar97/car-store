from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(CreateView):
    model = Car
    fields = ['model', 'brand', 'price', 'is_bought', 'buyer', 'buy_time']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    fields = ['model', 'brand', 'price', 'is_bought', 'buyer', 'buy_time']
    template_name = 'car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car_list')
