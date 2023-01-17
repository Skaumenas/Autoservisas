from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Paslauga, Automobilis, Uzsakymas, AutomobilisModelis, UzsakymoEilute
from django.views import generic


def index(request):
    num_paslaugos = Paslauga.objects.all().count()
    num_done_orders = UzsakymoEilute.objects.filter(status__exact="d").count()
    num_cars = Automobilis.objects.all().count()

    context = {"num_paslaugos": num_paslaugos,
               "num_done_orders": num_done_orders,
               "num_cars": num_cars
               }
    return render(request, "homepage.html", context=context)


def auto(request):
    auto_get = AutomobilisModelis.objects.all()
    context = {"autos": auto_get}
    return render(request, "auto.html", context=context)


def cars(request, cars_id):
    single_author = get_object_or_404(Automobilis, pk=cars_id)
    single_author2 = get_object_or_404(AutomobilisModelis, pk=cars_id)
    return render(request, "cars.html", {"cars": single_author, "autos": single_author2})


class OrderVievList(generic.ListView):
    model = Uzsakymas  # padaro uzsakymas_list
    template_name = 'orders.html'
