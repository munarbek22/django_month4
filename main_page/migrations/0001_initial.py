# Generated by Django 5.1.2 on 2024-11-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='book/', verbose_name='Загрузите картинку')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название книги')),
                ('description', models.TextField(verbose_name='Добавьте описание к фильму ')),
                ('price', models.FloatField(verbose_name='Укажите цену книги')),
                ('start_book', models.DateTimeField(verbose_name='Укажите дату выхода')),
                ('genre', models.CharField(choices=[('Литература', 'Литература'), ('Проза', 'Проза'), ('Саморазвитие', 'Саморазвитие')], default='Литература', max_length=100, verbose_name='Укажите жанр')),
                ('email', models.EmailField(max_length=254, verbose_name='Укажите почту автора')),
                ('author', models.CharField(max_length=30, verbose_name='Укажите имя автора')),
            ],
        ),
    ]
