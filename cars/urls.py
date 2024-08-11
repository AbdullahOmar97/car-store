from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView, CarViewSet

# Web views (HTML templates)
web_urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('create/', CarCreateView.as_view(), name='car_create'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
]

# API routes
router = DefaultRouter()
router.register(r'cars', CarViewSet)

api_urlpatterns = [
    path('', include(router.urls)),
]

# Combine both web views and API routes into a single urlpatterns list
urlpatterns = [
    path('cars/', include((web_urlpatterns, 'cars'), namespace='web')),
    path('api/', include((api_urlpatterns, 'cars'), namespace='api')),
]
