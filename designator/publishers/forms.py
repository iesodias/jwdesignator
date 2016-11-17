from django import forms

from designator.groups.models import Group


def c_gender():
    BLANK = "---"
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    gender_list = ((BLANK, '---'), (MASCULINO, 'Masculino'), (FEMENINO, 'Femenino'))
    return gender_list

def c_designation():
    BLANK = "---"
    ANCIAO = 'Ancião'
    SER_MIN = 'Servo Ministerial'
    PUBLIC = 'Publicador'
    designation_list = ((BLANK, '---'), (ANCIAO, 'Ancião'), (SER_MIN, 'Servo Ministerial'), (PUBLIC, 'Publicador'))
    return designation_list

def c_car():
    BLANK = "---"
    SIM = 'Sim'
    NAO = 'Não'
    c_list = ((BLANK, '---'), (SIM, 'Sim'), (NAO, 'Não'))
    return c_list


class PublisherForm(forms.Form):
    name = forms.CharField(label='Nome')
    address = forms.CharField(label='Endereço')
    phone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='Email')
    gender = forms.ChoiceField(label='Sexo', choices=c_gender())
    designation = forms.ChoiceField(label='Designação', choices=c_designation())
    group = forms.ModelChoiceField(label='Grupo', queryset=Group.objects.all().order_by('name'))
    car = forms.ChoiceField(label='Carrinho', choices=c_car())
