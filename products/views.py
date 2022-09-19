from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    new = Offer.objects.all
    return render(request, 'offer.html', {'new' : new})
