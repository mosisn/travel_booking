from django.urls import path
from .views import delete_trip, update_trip, create_trip, list_trip


urlpatterns = [
    path('', list_trip, name='list_trip'),
    path('new/', create_trip, name='create_trip'),
    path('<int:trip_id>/edit/', update_trip, name='update_trip'),
    path('<int:trip_id>/delete/', delete_trip, name='delete_trip'),
]