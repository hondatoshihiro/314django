from django import forms
from .models import Friend

class RecordLaptimeForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
