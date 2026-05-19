from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'location',
            'event_date'
        ]

        widgets = {

            'event_date': forms.DateInput(
                attrs={'type': 'date'}
            )

        }
