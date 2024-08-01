from django import forms
from .models import Trip
from django.utils import timezone

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'departure_date', 'return_date', 'number_of_travelers']
        widgets = {
            'departure_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        departure_date = cleaned_data.get("departure_date")
        return_date = cleaned_data.get("return_date")
        current_date = timezone.now().date()

        if departure_date < current_date:
            raise forms.ValidationError("Departure date cannot be in the past.")

        if return_date < current_date:
            raise forms.ValidationError("Return date cannot be in the past.")

        if return_date < departure_date:
            raise forms.ValidationError("Return date cannot be earlier than departure date.")

        return cleaned_data 