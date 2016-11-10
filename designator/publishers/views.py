from django.shortcuts import render
from designator.publishers.forms import PublisherForm

def publisher(request):
    context = {'form': PublisherForm()}
    return render(request, 'publishers/cadastro_form.html', context)


