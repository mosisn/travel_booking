from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from .forms import TripForm

def list_trip(request):
    trips = Trip.objects.all()
    context = {
        'trips' : trips
    }
    return render(request, 'templates/trip_list.html', context)

def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TripForm()
        return render(request, 'create_trip.html', {'form' : form})

def update_trip(request, trip_id):
    trip = get_object_or_404(Trip, id= trip_id)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
        return redirect('list_trip')
    else:
        form = TripForm(instance=trip)
        return render(request, 'templates/update_trip.html', {'form':form})

def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == 'POST':
        trip.delete()
        return redirect('list_trip')
    return render(request, 'delete_trip.html', {'trip':trip})