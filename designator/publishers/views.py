from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from designator.publishers.forms import PublisherForm
from designator.publishers.models import Publisher


def publisher(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
        form = PublisherForm(request.POST)
        if form.is_valid():
            messages.success(request,'Cadastro realizado com sucesso!')
            Publisher.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/cadastro/')
        else:
            return render(request, 'publishers/cadastro_form.html', {'form': form})

def new(request):
        return render(request, 'publishers/cadastro_form.html',
                      {'form': PublisherForm()})