from django import forms

class FormContact(forms.Form):
	name = forms.CharField(label='Nome')
	email = forms.EmailField(label='E-mail')
	phone = forms.CharField(label='Telefone', max_length=13)
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(), max_length=400)