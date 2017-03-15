from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calcula(request, sumando1, operador, sumando2):
    if operador == "+":
        res = int(sumando1)+int(sumando2)
    elif operador == "-":
        res = int(sumando1)-int(sumando2)
    elif operador == "*":
        res = int(sumando1)*int(sumando2)
    elif operador == "/":
        try:
            res = int(sumando1)/int(sumando2)
        except ZeroDivisionError:
            return HttpResponse('<h1>Quiero hacer ' +
                                sumando1 + operador + sumando2 +
                                '. Error: división entre 0</h1>')

    return HttpResponse('<h1><body>Calculadora</h1><p><b>' +
                        sumando1 + operador + sumando2 +
                        ' = ' + str(res) + '</b></p></body>')

def notfound(request, parametro):
    return HttpResponse('<h1>Not Found</h1>')
