from django.test import TestCase
from django.contrib.auth.models import User
from .models import Car
from django.urls import reverse
from datetime import datetime

class CarModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.car = Car.objects.create(
            model='Model X',
            brand='Tesla',
            price=99999.99,
            is_bought=True,
            buyer=self.user,
            buy_time=datetime(2024, 7, 22, 12, 0, 0)  # Use a datetime object here
        )

    def test_car_string_representation(self):
        self.assertEqual(str(self.car), 'Tesla Model X')

    def test_model_field(self):
        self.assertEqual(self.car.model, 'Model X')

    def test_brand_field(self):
        self.assertEqual(self.car.brand, 'Tesla')

    def test_price_field(self):
        self.assertEqual(self.car.price, 99999.99)

    def test_is_bought_field(self):
        self.assertTrue(self.car.is_bought)

    def test_buyer_field(self):
        self.assertEqual(self.car.buyer.username, 'testuser')

    def test_buy_time_field(self):
        expected_buy_time = datetime(2024, 7, 22, 12, 0, 0)
        self.assertEqual(self.car.buy_time, expected_buy_time)

class CarViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.car = Car.objects.create(
            model='Model X',
            brand='Tesla',
            price=99999.99,
            is_bought=True,
            buyer=self.user,
            buy_time='2024-07-22T12:00:00Z'
        )
        self.client.login(username='testuser', password='12345')

    def test_car_list_view(self):
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_list.html')
        self.assertContains(response, 'Model X')
        self.assertContains(response, 'Tesla')

    def test_car_detail_view(self):
        response = self.client.get(reverse('car_detail', args=[self.car.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'car_detail.html')
        self.assertContains(response, 'Model X')
        self.assertContains(response, 'Tesla')

    def test_car_create_view(self):
        response = self.client.post(reverse('car_create'), {
            'model': 'Model Y',
            'brand': 'Tesla',
            'price': 109999.99,
            'is_bought': False,
            'buyer': self.user.pk,
            'buy_time': '2024-07-23T12:00:00Z',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to the list view
        self.assertTrue(Car.objects.filter(model='Model Y').exists())

    def test_car_update_view(self):
        response = self.client.post(reverse('car_update', args=[self.car.pk]), {
            'model': 'Model Z',
            'brand': 'Tesla',
            'price': 119999.99,
            'is_bought': True,
            'buyer': self.user.pk,
            'buy_time': '2024-07-24T12:00:00Z',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to the list view
        self.car.refresh_from_db()
        self.assertEqual(self.car.model, 'Model Z')

    def test_car_delete_view(self):
        response = self.client.post(reverse('car_delete', args=[self.car.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect to the list view
        self.assertFalse(Car.objects.filter(pk=self.car.pk).exists())
