from django.db import models

class Group(models.Model):
    name = models.CharField('nome', max_length=100)
    address = models.CharField('endereco', max_length=100)
    sup_group = models.CharField('superintendente de grupo', max_length=20)

    class Meta:
        verbose_name_plural = 'grupos'
        verbose_name = 'grupo'

    def __str__(self):
        return self.name