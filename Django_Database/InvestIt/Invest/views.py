from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Stocks
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


@csrf_exempt
def add_stock(request):
    if request.method == 'POST':
        stock_name = request.POST.get("stock_name")
        buy_price = request.POST.get("buy_price")
        quantity = request.POST.get("buy_quantity")
        buy_date = request.POST.get("buy_date")
        u = User.objects.get(id=1)
        check_data_exists = Stocks.objects.filter(user=u, name=stock_name,buy_price=buy_price, buy_date=buy_date, quantity=quantity).exists()
        if check_data_exists:
            return HttpResponse("Stock Already Exists. Please Edit it")
        else:
            try:
                total_amount = buy_price*quantity
                data = Stocks.objects.create(user=u, name=stock_name,buy_price=buy_price, buy_date=buy_date, quantity=quantity,total_amount=total_amount)
                print(data)
                return HttpResponse("Success")
            except ValidationError:
                return HttpResponse("Something is Wrong with the Data")
    else:
        return HttpResponse('Something went wrong')


def display_stocks(request):
    # always send the current user id from javascript
    stocks = Stocks.objects.filter(user__id=1).values()
    print(stocks)
    return JsonResponse({'value':list(stocks)})
