from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def pago_diferido(request):
    return render(request, 'home/pago_diferido.html')


def pago_programado(request):
    return render(request, 'home/pago_programado.html')


def debito(request):
    return render(request, 'home/debito.html')


def credito(request):
    return render(request, 'home/credito.html')


def suscripcion(request):
    return render(request, 'home/suscripcion.html')


def puntaje(request):
    return render(request, 'home/puntaje.html')
