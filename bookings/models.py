from django.db import models
from django.core.exceptions import ValidationError

class Trip(models.Model):
    destination = models.CharField (max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField()
    number_of_travelers = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.return_date < self.departure_date:
            raise ValidationError('Return date cannot be earlier than departure date.')
        if self.number_of_travelers <= 0:
            raise ValidationError('Number of travelers must be one or more.')
    def __str__(self):
        return f"{self.destination} ({self.departure_date} to {self.return_date})"