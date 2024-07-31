from django.contrib.admin import ModelAdmin, register
from .models import Trip


@register(Trip)
class TripAdmin(ModelAdmin):
    pass