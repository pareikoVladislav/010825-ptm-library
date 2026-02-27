from datetime import date
from django.core.validators import MaxValueValidator
from django.db import models


class Book(models.Model):
    CHOICE_GENRE = [
        ("N/A", "Not Selected"),
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Biography', 'Biography'),
    ]

    name:str = models.CharField(max_length=100, verbose_name="Название книги")
    author: 'Author' = models.ForeignKey(to='Author', on_delete=models.SET_NULL, null=True, related_name='books')
    published_date:date = models.DateField(verbose_name="Дата публикации")
    library = models.ManyToManyField('library.Library', related_name='books')
    description: str = models.TextField(verbose_name="Описание книги", null=True, blank=True)
    genre: str = models.CharField(max_length=50, verbose_name="Жанр", choices=CHOICE_GENRE, default='N/A')
    pages: int = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10000)], verbose_name="кол-во страниц", null=True, blank=True)