from cities_light.models import Country, City
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ChoiceField

from user.models import Registration

User = get_user_model()


class UserCreationForm(forms.ModelForm):

    country = ChoiceField(required=True)
    city = ChoiceField(required=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].required = True
        self.fields['email'].required = True
        self.fields['contact_number'].required = True
        self.fields["country"].choices = [("", "Select")] + list(
            Country.objects.values_list('name', 'name'))
        self.fields["city"].choices = [("", "Select")] + list(
            City.objects.values_list('name', 'name'))

    # create meta class
    class Meta:
        # specify model to be used
        model = Registration
        # specify fields to be used
        exclude = ("id", )
