from django import forms
from .models import Appointment

class SuggestionForm(forms.ModelForm):

    suggestion = forms.CharField(widget=forms.Textarea)
    prescription = forms.FileField()

    class Meta:
        model = Appointment
        fields = ('suggestion', 'prescription')