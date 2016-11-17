from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from designator.groups.forms import GroupForm
from designator.groups.models import Group


def group(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
        form = GroupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Cadastro realizado com sucesso!')
            Group.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/grupos/')
        else:
            return render(request, 'groups/groups_form.html', {'form': form})


def new(request):
    return render(request, 'groups/groups_form.html',
                  {'form': GroupForm()})