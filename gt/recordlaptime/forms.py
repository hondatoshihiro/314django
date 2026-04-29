from django import forms

class RecordLaptimeForm(forms.Form):
    id = forms.IntegerField(label='ID')
