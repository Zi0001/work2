from  django import forms

from .models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('name', 'completed_work', 'place_of_work')