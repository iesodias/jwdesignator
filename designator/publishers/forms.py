from django import forms

class PublisherForm(forms.Form):
    name = forms.CharField(label='Nome')
    address = forms.CharField(label='Endereço')
    phone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='Email')
    gender = forms.CharField(label='Sexo')
    designation = forms.CharField(label='Designação')
    group = forms.CharField(label='Grupo')
    car = forms.CharField(label='Carrinho')
