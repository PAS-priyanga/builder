# forms.py

from django.forms import ModelForm
from .models import PropertyDetails

class PropertyDetailsForm(ModelForm):
  class Meta:
    model = PropertyDetails
    fields = ['last_built_year', 'last_property_size']
