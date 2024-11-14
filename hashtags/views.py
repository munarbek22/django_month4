from django.shortcuts import render
from . import models

def all_clothes_list_view(request):
    if request.method == 'GET':
        clothes_list = models.Clothes.objects.filter().order_by('-id')
        context = {'clothes_list': clothes_list}
        return render(request, 'all_clothes_list_view.html',
                      context=context)

def elderly_people_clothes(request):
    if request.method == 'GET':
        elderly_people = models.Clothes.objects.filter(tags__name='для стариков').order_by('-id')
        context = {'elderly_people': elderly_people}
        return render(request, 'elderly_people.html',
                      context=context)

def young_people_clothes(request):
    if request.method == 'GET':
        young_people = models.Clothes.objects.filter(tags__name='для молодых').order_by('-id')
        context = {'young_people': young_people}
        return render(request, 'young_people.html',
                      context=context)

def kids(request):
    if request.method == 'GET':
        kids = models.Clothes.objects.filter(tags__name='для детей').order_by('-id')
        context = {'kids': kids}
        return render(request, 'kids.html',
                      context=context)