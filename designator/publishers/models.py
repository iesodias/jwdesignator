from django.db import models

class Publisher(models.Model):
    name = models.CharField('nome', max_length=100)
    address = models.CharField('endereço', max_length=100)
    phone = models.CharField('telefone', max_length=20)
    email = models.EmailField('e-mail')
    gender = models.CharField('sexo', max_length=30)
    designation = models.CharField('designacao', max_length=30)
    group = models.CharField('grupo', max_length=30)
    car = models.CharField('carrinho', max_length=30)

    class Meta:
        verbose_name_plural = 'Publicadores'
        verbose_name = 'Publicador'

    def __str__(self):
        return self.name