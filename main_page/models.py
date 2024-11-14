from django.core.validators import MinValueValidator, MaxValueValidator
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

    def average_raiting(self):
        reviews =self.review_books.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    class Meta():
        verbose_name = "книга"
        verbose_name_plural = "книги"

    def __str__(self):
        return f'{self.title} - {self.price}сом'

class ReviewBook(models.Model):
    review_books = models.ForeignKey(Library, on_delete=models.CASCADE,
                                     related_name='review_boks')
    created_at = models.DateField(auto_now_add=True)
    descripton = models.TextField(verbose_name='Оставьте отзыв о книге')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_books} - {self.created_at}'
    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментрии'