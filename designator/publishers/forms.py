from django import forms

choice_gender = (
    ('0', ''),
    ('1', 'Masculino'),
    ('2', 'Feminino'),
)

choice_designation = (
    ('1', ''),
    ('2', 'Ancião'),
    ('3', 'Servo Ministerial'),
)

#Criar uma queryset para buscar no cadastro de grupos
choice_group = (
    ('1', 'Make a Queryset'),
)

choice_car = (
    ('1', ''),
    ('2', 'Sim'),
    ('3', 'Não'),
)

class PublisherForm(forms.Form):
    name = forms.CharField(label='Nome')
    address = forms.CharField(label='Endereço')
    phone = forms.CharField(label='Telefone')
    email = forms.EmailField(label='Email')
    gender = forms.ChoiceField(choice_gender, label='Sexo')
    designation = forms.ChoiceField(choice_designation, label='Designação')
    group = forms.ChoiceField(choice_group, label='Grupo')
    car = forms.ChoiceField(choice_car, label='Carrinho')
