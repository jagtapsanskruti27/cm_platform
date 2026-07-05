from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [

            "title",

            "description",

            "banner",

            "category",

            "event_type",

            "address",

            "google_map_link",

            "start_datetime",

            "end_datetime",

            "registration_deadline",

            "capacity",

            "is_public",

        ]

        widgets = {

            "start_datetime": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),

            "end_datetime": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),

            "registration_deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),

        }