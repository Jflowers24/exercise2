from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def calc(request: HttpsRequest, end: int, birthyear: int)-> HttpResponse:
    endyear = end
    birth = birthyear
    result = endyear - birth
    return HttpResponse(result)


def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World")


def hi_name(request: HttpRequest, name: str)-> HttpResponse :
    user = name.upper()
    return HttpResponse(f"Hey, {name}!")


def order(request: HttpRequest, burgers: int, fries: int, drinks: int)-> HttpResponse:
    frynum = fries
    burgnum = burgers
    drinknum = drinks
    frytotal = frynum * 1.5
    burgtotal = burgnum * 4.50
    drinktotal = drinknum * 1

    ordertotal = (frytotal + burgtotal + drinktotal,)

    return HttpResponse(ordertotal)


def addnum(request: HttpRequest, num1: int, num2: int)-> HttpResponse:
    x = num1
    y = num2
    totat = x + y
    return HttpResponse(totat)
