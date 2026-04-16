from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('book/<int:id>/', views.book_car, name='book_car'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]