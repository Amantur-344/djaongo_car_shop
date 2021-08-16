from django import forms

from cars.models import Car


class CarCreateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('category', 'title', 'description', 'engine', 'price', 'image', 'release_auto', 'color', 'transmission', 'rul')


class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('category', 'title', 'description', 'engine', 'price', 'image', 'release_auto', 'color', 'transmission', 'rul')
