from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def calc(request, end, birthyear):
    endyear = end
    birth = birthyear
    result = endyear - birth
    return HttpResponse(result)


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


def hi_name(request, name):
    user = name.upper()
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


def addnum(request, num1, num2):
    x = num1
    y = num2
    totat = x + y
    return HttpResponse(totat)
