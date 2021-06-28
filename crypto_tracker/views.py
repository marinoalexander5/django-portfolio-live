from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

    context = {
        'data': data
    }

    return render(request, "crypto_tracker/main.html", context)