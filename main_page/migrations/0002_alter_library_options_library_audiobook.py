# Generated by Django 5.1.2 on 2024-11-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
        migrations.AddField(
            model_name='library',
            name='audiobook',
            field=models.URLField(null=True, verbose_name='Укажите аудиокнигу с youtube'),
        ),
    ]
