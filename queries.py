import os
import django
from datetime import date
import random
import math

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

from library.models.member import Member
from library.models.authors import Author
from library.models.library import Library
from library.models.books import Book
from library.models.borrow import Borrow

# member = Member.objects.create(
#     email="new_member@test.com",
#     role="member",
#     first_name="John",
#     last_name="Doe",
#     gender="male",
#     age=date.today().year - date(1999, 1, 1).year - ((date.today().month, date.today().day) < (date(1999, 1, 1).month, date(1999, 1, 1).day)),
#     birth_date=date(1999, 1, 1)
# )

# count = Author.objects.count()
# random_index = random.randint(1,count-1)

# update_author = Author.objects.all()[random_index]
# print(update_author.name, update_author.rating)
# update_author.rating = 9.5
# update_author.save()

# print(update_author.name, update_author.rating)


# **ТЗ:**
# 1. Найти все книги категории с названием, содержащим 'Fiction'
# 2. Исключить книги с количеством страниц меньше 200
# 3. Подсчитать количество таких книг

# books_count = Book.objects.filter(
#     category__name__icontains = 'Fiction'
# ).exclude(
#     pages__lt = 200
# ).count()


# **ТЗ:**
# 1. Найти всех членов библиотеки, которые являются либо администраторами, либо сотрудниками
# 2. Исключить неактивных членов
# 3. Отсортировать по фамилии и имени

# members = (
#     Member.objects.filter(role__in=["admin", "staff"])
#     .exclude(is_active=False)
#     .order_by("last_name", "first_name")
# )

# members = (
#     Member.objects.filter(role__in=["admin", "staff"], is_active=True)
#     .order_by("last_name", "first_name")
# )

# author = Author.objects.filter(
#     name__startswith='A'
# )

# rating = Author.objects.filter(
#     rating__gt=8.5
# )

# birth_year = Author.objects.filter(
#     #date_for_birth__year__gt=1950,
#     date_for_birth__gt="1950-12-10",
# )

# first_author = author.first()

# for obj in author:
#     print(obj.name,obj.rating)

# print(author)
# print(rating)
# print(birth_year)
# print(first_author)


# **ТЗ:**
# 1. Найти книги, название которых содержит слово 'The' (регистронезависимо)
# 2. Исключить книги с количеством страниц меньше 200
# 3. Найти книги, опубликованные в определенном диапазоне дат
# 4. Отсортировать по количеству страниц (по убыванию)

# books = Book.objects.filter(
#     name__icontains='The'
# ).exclude(
#     pages__lt=200
# ).filter(
#     published_date__range=(date(2000,1,1), date(2020,1,1))
# ).order_by('-pages')


# books = Book.objects.filter(
#     name__icontains='The',
#     pages__gt=200
# ).filter(
#     published_date__range=(date(2000,1,1), date(2020,1,1))
# ).order_by('-pages')


# books_300 = Book.objects.filter(
#     name__icontains='the',
#     page__gt=300
# ).order_by(
#     '-published_date'
# )

# authors_rating_9 = Author.objects.filter(
#     rating__gt=9,
#     date_for_birth__year__gt=1970
# ).order_by(
#     "-rating"
# )

# books_2010 = Book.objects.filter(
#     published_date__year__gt=2010,
#     page__range=(200,500)
# )

# active_member = Member.objects.filter(
#     # role__in=['member'],
#     role="member",
#     is_active=True
# ).order_by(
#     "last_name","first_name"
# )

# # часть 2 - джоины

# books_author_8 = Book.objects.filter(
#     author__rating__gt=8
# )

# publisher_germany = Book.objects.filter(
#     publisher__country="Germany"
# )

# books_fantasy = Book.objects.filter(
#     category__name="Fantasy"
# ).order_by(
#     '-author__rating'
# )

# member_in_library = Member.objects.filter(
#     library__name="Central Library"
# )

# author_pages_500 = Author.objects.filter(
#     book__pages__gt=400
# ).distinct()


# **ТЗ:**
# 1. Найти все займы (Borrow), которые не возвращены (is_returned=False)
# 2. Среди них найти те, где return_date уже прошла (меньше текущей даты)
# 3. Исключить займы, где return_date равно None
# 4. Отсортировать по дате займа (старые первыми)

# borrows = (
#     Borrow.objects.filter(
#         is_returned=False,
#         end_plane_date__lt=date.today(),
#         end_plane_date__isnull=False
#     )
#     .order_by("end_plane_date")
# )


# **ТЗ:**
# 1. Найти активных авторов с рейтингом от 8.0 до 9.5 включительно
# 2. Среди них найти тех, кто родился в XX веке (1901-2000 годы)
# 3. Исключить авторов без указанной даты рождения
# 4. Получить только первые 10 результатов


# authors = Author.objects.filter(
#     rating__range=(8,9.5),
#     date_for_birth__isnull=False,
#     date_for_birth__range=(date(1901,1,1),date(2000,12,31)),
# )[:10]

# print(authors.query)

# for author in authors:
#     print(f"{author.name=},{author.rating=},{author.date_for_birth=}",sep='\n')

# ================
from django.db.models import Count, Min, Max, Avg, Sum

# ### **Задача 1: Общее количество книг и среднее кол-во страниц**
# **ТЗ:** Получить общее количество книг в базе данных и среднее кол-во страниц всех книг в одном запросе

# result = Book.objects.aggregate(total_books=Count("id"), avg_pages=Avg("pages"))


### **Задача 2: Диапазон страниц**
# **ТЗ:** Найти минимальное кол-во, максимальное кол-во сраниц среди всех книг

# pages_range = Book.objects.aggregate(
#     min_pages=Min("pages"),
#     max_pages=Max("pages"),
# )

### **Задача 3: Количество книг по каждому жанру**
# **ТЗ:** Подсчитать количество книг в каждом жанре, отсортировать по убыванию количества

# count_book_genre = (
#     Book.objects.values("genre").annotate(count=Count("genre")).order_by("-count")
# )

### **Задача 4: Средняя цена книг по каждому издательству**
# **ТЗ:** Вычислить среднюю цену книг для каждого издательства и количество книг у каждого издательства

# avg_price_by_publisher = Book.objects.values("publisher").annotate(
#     avg_price=Avg("price"), book_count=Count("id")
# )
### **Задача 6: Топ-5 читателей по количеству активных займов**
# **ТЗ:** Найти 5 пользователей с наибольшим количеством невозвращенных книг -- Keteryna

# members = Member.objects.aggregate


# Задача 1
# 👉 Найти:
# общее количество книг
# общее количество страниц
# среднюю цену
# 👉 в одном запросе

# result = Book.objects.aggregate(
#     book_count=Count("id"), page_count=Sum("pages"), avg_price=Avg("price")
# )
# Задача 2
# 👉 Найти:
# количество книг с ценой
# количество книг без цены
# 💡 намёк: filter внутри Count


# books = Book.objects.aggregate(
#     book_with_price=Count("price", filter=Q(price__isnull=False)),
#     book_without_price=Count("price", filter=Q(price__isnull=True)),
# )
# Задача 3
# 👉 Для каждого жанра:
# количество книг
# среднее количество страниц
# 👉 отсортировать по убыванию среднего числа страниц

# result = (
#     Book.objects.values("category")
#     .annotate(book_count=Count("id"), avg_pages=Avg("pages"))
#     .order_by("-avg_pages")
# )

# Задача 4
# 👉 Для каждого автора:
# количество книг
# максимальное количество страниц
# 👉 оставить только авторов, у которых:
# больше 1 книги
# и максимальное число страниц > 300


# result = Author.objects.annotate(
#     books_count=Count("books"), max_pages=Max("books__pages")
# ).filter(books_count__gt=1, max_pages__gt=300)
# Задача 5
# 👉 Для каждого издательства (publisher):
# средняя цена
# минимальная цена
# максимальная цена
# 👉 отсортировать по средней цене (убывание)


# result = (
#     Book.objects.values("publisher")
#     .annotate(avg_price=Avg("price"), min_price=Min("price"), max_price=Max("price"))
#     .order_by("-avg_price")
# )

# Задача 6
# 👉 Найти:
# автора с максимальным количеством книг
# 💡 тут уже не просто annotate → придётся подумать

# result = (
#     Author.objects.annotate(books_count=Count("books_id"))
#     .order_by("-books_count")
#     .first()
# )

### **Задача 10: Книги дороже средней цены в своем жанре**
# **ТЗ:** Найти книги, цена которых превышает среднюю цену книг в том же жанре

from django.db.models import OuterRef, Subquery, Q, F

avg_price = (
    Book.objects.filter(category=OuterRef("category"))
    .values("category")
    .annotate(avg_price=Avg("price"))
    .values("avg_price")
)

books = Book.objects.annotate(avg_price=Subquery(avg_price)).filter(
    price__gt=F("avg_price"),
)

for book in books:
    print(f"{book.name} - {book.price} > {book.avg_price}")