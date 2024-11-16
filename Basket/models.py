from django.db import models
from main_page.models import Library


class Order(models.Model):
    name = models.CharField(max_length=30, verbose_name='Укажите имя заказчика')
    phone_number = models.IntegerField(verbose_name='Укажите ваш номер')
    email = models.EmailField(verbose_name='Уажите вашу почту')
    book = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Заказ от {self.name} на {self.book}"


