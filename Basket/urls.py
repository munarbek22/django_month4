from django.urls import path
from . import views

urlpatterns = [
    path('order_list/', views.order_list, name='order_list'),
    path('delete_order/int:id/delete/', views.delete_order_view, name='delete'),
    path('update_order/int:id/update/', views.update_order_view, name='update'),
    path('create_order/', views.create_order_view, name='create_order')
]