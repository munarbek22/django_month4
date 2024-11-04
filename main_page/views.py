from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Привет, я Мунарбек и я изучаю пайтон')

def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("имя  питомца - Хатико, фото питомца-<img src = 'https://www.princeton.edu/sites/default/files/styles/1x_full_2x_half_crop/public/images/2022/02/KOA_Nassau_2697x1517.jpg?itok=Bg2K7j7J' >")

def system_time(request):
    current_data = datetime.now()
    if request.method == 'GET':
        return HttpResponse(f'текущее время: {current_data}')