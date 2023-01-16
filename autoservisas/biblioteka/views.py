from django.http import HttpResponse
from django.shortcuts import render
from .models import Paslauga, Automobilis, Uzsakymas, AutomobilisModelis, UzsakymoEilute


def index(request):
    num_paslaugos = Paslauga.objects.all().count()
    num_done_orders = UzsakymoEilute.objects.filter(status__exact="d").count()
    num_cars = Automobilis.objects.all().count()

    context = {"num_paslaugos": num_paslaugos,
               "num_done_orders": num_done_orders,
               "num_cars": num_cars
               }
    return render(request, "homepage.html", context=context)
