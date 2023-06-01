from django.shortcuts import render, redirect
from phones.models import Phone
import csv


def index(request):    
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = str(request.GET.get("sort"))
    if sort == 'name':
        phones = sorted(phones, key=lambda x: x.name)
    elif sort == 'min_price':
        phones = sorted(phones, key=lambda x: x.price)
    elif sort == 'max_price':
        phones = sorted(phones, key=lambda x: x.price, reverse=True)
    context = {
        'phones' : phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone' : phone,
    }
    return render(request, template, context)
