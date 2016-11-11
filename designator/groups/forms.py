from django import forms

class GroupForm(forms.Form):
    name = forms.CharField(label='Nome')
    address = forms.CharField(label='Endereço')
    sup_group = forms.CharField(label='Superintendente de Grupo')
