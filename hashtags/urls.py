from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes_list_view, name='all_clothes_tags'),
    path('elderly_people/', views.elderly_people_clothes, name='elderly_people'),
    path('young_people/', views.young_people_clothes, name='young_people'),
    path('kids/', views.kids, name='kids'),

]