from django.shortcuts import render
from designator.groups.forms import GroupForm


def group(request):
    context = {'form': GroupForm()}
    return render(request, 'groups/groups_form.html', context)