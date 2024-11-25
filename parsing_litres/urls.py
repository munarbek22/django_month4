from django.urls import path
from . import views

urlpatterns = [
    path('litres_list/', views.LitresListView.as_view(), name='litres_list'),
    path('litres_parser/', views.LitresFormView.as_view(), name='litres_parser'),
]