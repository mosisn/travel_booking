# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TripView

router = DefaultRouter()
router.register(r'trips', TripView)

urlpatterns = [
    path('', include(router.urls)),
]
