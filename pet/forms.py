from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = [
            'type',
            'breed',
            'name',
            'age',
            'description',
            'image'
        ]