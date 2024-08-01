# myapp/serializers.py
from rest_framework import serializers
from bookings.models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['id', 'destination', 'departure_date', 'return_date', 'number_of_travelers']
