from django.urls import path
from .views import main_page, car_delete, car_update, car_detail, category_cars, my_cars, create_car, search, \
    expensive_cars, user_cars

urlpatterns = [
    path('car-delete/<int:pk>/', car_delete, name='car_delete'),
    path('car-update/<int:pk>/', car_update, name='car_update'),
    path('car-detail/<int:pk>/', car_detail, name='car_detail'),
    path('category/<int:pk>/', category_cars, name='category_details'),
    path('expensive-cars/', expensive_cars, name='expensive_cars'),
    path('my-cars/', my_cars, name='my_cars'),
    path('user-cars/<int:pk>/', user_cars, name='user_cars'),
    path('create-car/', create_car, name='car_create'),
    path('search/', search, name='search'),
    path('', main_page, name='main_page'),
]
