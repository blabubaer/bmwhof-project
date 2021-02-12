from django.forms import ModelForm
from .models import Part


class PartForm(ModelForm):
    class Meta:
        model = Part
        fields = ['part_number','name','category','car_model','count','description','image']
