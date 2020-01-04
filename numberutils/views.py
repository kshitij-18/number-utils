from django.http import HttpResponse
from django.shortcuts import render
from . import extracter


def index(request):
    # return HttpResponse('Hi this is the home page')
    return render(request, 'index.html')


def analyzer(request):
    # get the number
    num = request.POST.get('text', 'default')

    # checking for options
    square = request.POST.get('squaring', 'off')
    cube = request.POST.get('cubing', 'off')
    currency = request.POST.get('currency_convert', 'off')

    # check if the user forgot to enter or has not entered a number
    if len(num) == 0:
        return HttpResponse("Please enter something")
    try:
        num = int(num)
        if square == "on":
            result = num**2
            params = {'purpose': 'Squaring', 'result': result}
            return render(request, 'analyze.html', params)
        if cube == "on":
            result = num**3
            params = {'purpose': 'Cubing', 'result': result}
            return render(request, 'analyze.html', params)
        if currency == 'on':
            params = {'purpose': 'Currency Conversion',
                      'result': f'USD {extracter.exchange(num)}'}
            return render(request, 'analyze.html', params)
    except ValueError:
        return render(request, 'confirm.html')

    return HttpResponse("num returned at terminal")
