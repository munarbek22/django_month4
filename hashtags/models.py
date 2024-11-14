from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Clothes(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField(default=100)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

Список комментариев с рейтингом
comments = [
    {"text": "Отличная книга!", "rating": 5},
    {"text": "Очень интересно.", "rating": 4},
    {"text": "Не понравилось.", "rating": 2},
    {"text": "Хорошая книга.", "rating": 4},
    {"text": "Пойдет.", "rating": 3},
    {"text": "Замечательная история.", "rating": 5},
    {"text": "Скучновато.", "rating": 3}
]

# Функция для подсчета среднего рейтинга последних 5 комментариев
def calculate_average_rating(comments):
    last_five_comments = comments[-5:]
    total_rating = sum(comment["rating"] for comment in last_five_comments)
    average_rating = total_rating / len(last_five_comments)
    return average_rating, last_five_comments

# Получение среднего рейтинга и отображение последних 5 комментариев
average, last_five = calculate_average_rating(comments)
print(f"Средний рейтинг последних 5 комментариев: {average:.2f}")
print("Последние 5 комментариев:")
for comment in last_five:
    print(f"- {comment['text']} (Рейтинг: {comment['rating']})")
