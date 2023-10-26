from django.apps import AppConfig
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

def calc(request, end, birthyear):
    endyear = end
    birth = birthyear
    result = endyear - birth
    return HttpResponse(result)


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


def hi_name(request, name):
    user = name
    return HttpResponse(f"Hey {name}")


def order(request, burgers, fries, drinks):
    frynum = fries
    burgnum = burgers
    drinknum = drinks
    frytotal = frynum * 1.5
    burgtotal = burgnum * 4.50
    drinktotal = drinknum * 1

    ordertotal = (frytotal + burgtotal + drinktotal,)

    return HttpResponse(ordertotal)
