from django import forms

def c_gender():
    MASCULINO = 'Masculino'
    FEMENINO = 'Femenino'
    gender_list = ((MASCULINO, 'Masculino'), (FEMENINO, 'Femenino'))
    return gender_list

def c_designation():
    ANCIAO = 'Ancião'
    SER_MIN = 'Servo Ministerial'
    designation_list = ((ANCIAO, 'Ancião'), (SER_MIN, 'Servo Ministerial'))
    return designation_list

def c_car():
    SIM = 'Sim'
    NAO = 'Não'
    c_list = ((SIM, 'Sim'), (NAO, 'Não'))
    return c_list


class PublisherForm(forms.Form):
    name = forms.CharField(label='Nome')
    address = forms.CharField(label='Endereço')
    phone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='Email')
    gender = forms.ChoiceField(label='Sexo', choices=c_gender())
    designation = forms.ChoiceField(label='Designação', choices=c_designation())
    group = forms.CharField(label='Grupo')
    car = forms.ChoiceField(label='Carrinho', choices=c_car())
