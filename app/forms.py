# app/forms.py

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

    def clean_profile_picture(self):
        image = self.cleaned_data.get('profile_picture')

        if image:

            if image.content_type not in [
                'image/jpeg',
                'image/png'
            ]:
                raise forms.ValidationError(
                    "Only JPG and PNG allowed"
                )

            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image must be less than 2MB"
                )

        return image