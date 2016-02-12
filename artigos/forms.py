from django import forms

class FormContact(forms.Form):
	name = forms.CharField()
	email = forms.EmailField(required=False)
	phone = forms.CharField(label='Telefone', max_length=13)
	message = forms.CharField(widge=forms.TextArea(), max_length=400)