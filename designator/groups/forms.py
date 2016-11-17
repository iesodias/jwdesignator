from django import forms
from designator.publishers.models import Publisher

def SupGroup():
    suplist = Publisher.objects.all().order_by('name')
    return suplist

def SupList():
    qs = Publisher.objects.all().order_by('name')
    values = ['name', 'gender']
    return qs.values(*values)

class GroupForm(forms.Form):
    name = forms.CharField(label='Nome do Grupo')
    address = forms.CharField(label='Endereço')
    sup_group = forms.ModelChoiceField(label='Superintendente de Grupo', queryset=Publisher.objects.filter(gender='Masculino', designation='Ancião').order_by('name'))
