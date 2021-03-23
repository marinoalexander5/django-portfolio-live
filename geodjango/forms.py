from django import forms
from django.forms import TextInput
from .models import Measurement

class MeasurementModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MeasurementModelForm, self).__init__(*args, **kwargs)
        self.fields['destination'].widget.attrs['placeholder'] = 'Enter destination. (i.e.: Antarctica)'
    class Meta:
        model = Measurement
        fields = ('destination',)