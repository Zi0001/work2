from  django import forms

from .models import Journal

class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('problem',)

class EditRecord(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ('place', 'executor')
