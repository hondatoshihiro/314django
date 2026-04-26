from django import forms

class RecordLaptimeForm(forms.Form):
    #widget引数：forms.TextInputで<input type="text">のウィジェット
    #forms.NumberINputで<input type="number">のウィジェットを埋め込む
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='mail', widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age', widget=forms.NumberInput(attrs={'class':'form-control'}))
