from django.urls import path
from . import views

urlpatterns =[
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>', views.book_detail_view, name='detail'),
]