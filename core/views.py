from django.shortcuts import render


def inicio(request):
    return render(request, 'core/home.html')


def casas(request):
    return render(request, 'core/casas.html')


def sobre(request):
    return render(request, 'core/sobre.html')
