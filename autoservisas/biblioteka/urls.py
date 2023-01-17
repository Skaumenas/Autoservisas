from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.auto, name='auto'),
    path('auto/<int:cars_id>', views.cars, name="cars-detail"),
    path('orders/', views.OrderVievList.as_view(), name='order')
]
