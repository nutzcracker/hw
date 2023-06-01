from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open ('data-398-2018-08-30.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        CONTENT = reader

        print(CONTENT)
        
        paginator = Paginator(CONTENT, 5)
        page_number = request.GET.get("page", 1)
        page = Paginator.get_page(page_number)
        context = {
            'bus_stations': reader,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
