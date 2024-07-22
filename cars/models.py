from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_bought = models.BooleanField()
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    buy_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model}'
    
    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})
