from django.shortcuts import render

# Create your views here.


def linkar_index(request):
    return render(request, 'index.html')

def retornar_nomes(request):
    return render(request, 'nomes.html')