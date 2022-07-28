from django import forms
from django.urls import reverse
from .models import Animal, SitingList, Breed


class DateInput(forms.DateInput):
    """ Custom date field - HTML5"""
    input_type = 'date'


class SitingListForm(forms.ModelForm):
    """ Form for sitting list"""

    # Extra Field
    animals = Animal.objects.all()
    animal = forms.ChoiceField(choices=tuple([(u'', 'Select Animal')] + list(animals.values_list('id', 'name'))),
                               widget=forms.Select(attrs={'hx-post': '/get-breed-data/',
                                                          'hx-trigger': 'change',
                                                          'hx-target': '#id_breed'}))

    class Meta:
        """ Form information """
        model = SitingList
        fields = ('breed', 'created')
        widgets = {
            'created': DateInput()
        }

    field_order = ['animal', 'breed', 'created']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['breed'].queryset = Breed.objects.none()


class SitingListForm2(SitingListForm):
    animals = Animal.objects.all()
    animal = forms.ChoiceField(choices=tuple([(u'', 'Select Animal')] + list(animals.values_list('id', 'name'))),
                               widget=forms.Select(attrs={'onchange': 'get_breed();'}))
