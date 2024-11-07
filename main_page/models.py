from django.db import models

class Library(models.Model):
    GENRE_CHOICE = (
        ('Литература','Литература'),
        ('Проза','Проза'),
        ('Саморазвитие','Саморазвитие')
    )
    image = models.ImageField(upload_to='book/', verbose_name='Загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Добавьте описание к фильму ')
    price = models.FloatField(verbose_name='Укажите цену книги')
    start_book = models.DateTimeField(verbose_name='Укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Литература',
                             verbose_name='Укажите жанр')
    email = models.EmailField(verbose_name='Укажите почту автора')
    author = models.CharField(max_length=30, verbose_name='Укажите имя автора')
    audiobook = models.URLField(verbose_name='Укажите аудиокнигу с youtube', null=True)

    class Meta():
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return f'{self.title} - {self.price}сом'