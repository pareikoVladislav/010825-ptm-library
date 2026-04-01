import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

"""Общее количество книг и среднее кол-во страниц**
# **ТЗ:** Получить общее количество книг в базе данных и среднее кол-во страниц всех книг в одном запросе"""
from library.models import Book, Author, Member
from django.db.models import Count, Avg, Max, Min, Q, OuterRef, Subquery, F, FloatField
from django.db.models.functions import Cast
query = Book.objects.aggregate(
    book_count=Count('id'),
    avg_pages= Avg('pages'))

#print(query)
#print(query['book_count'], query['count_pages'])

"""Диапазон страниц**
# **ТЗ:** Найти минимальное кол-во, максимальное кол-во сраниц среди всех книг """
query2 = Book.objects.aggregate(
    pages_min=Min('pages'),
    pages_max= Max('pages'))

print(query2)
"""Количество книг по каждому жанру**
# **ТЗ:** Подсчитать количество книг в каждом жанре, отсортировать по убыванию количества"""

query3 = Book.objects.values('genre').annotate(tot=Count('id')).order_by('-tot')
#print(query3)


"""Средняя цена книг по каждому издательству**
# **ТЗ:** Вычислить среднюю цену книг для каждого издательства и количество книг у каждого издательства"""
query4= Book.objects.values('publisher').annotate(books_count= Count("id"), avg_price=Avg('price'))

#print(query4)


"""Авторы с количеством книг и средним рейтингом**
# **ТЗ:** Получить всех авторов с количеством написанных книг, отсортировать по убыванию количества книг"""


query5 = Author.objects.annotate(books_count=Count('books')).order_by('-books_count')
#print(query5)
#print(query5.query)
#for i in query5:

    #print(f"surname: {i.surname}, books_count: {i.books_count}")

"""читателей по количеству активных займов**
# **ТЗ:** Найти 5 пользователей с наибольшим количеством невозвращенных книг """
### **Задача 6: Топ-5 читателей по количеству активных займов**
# **ТЗ:** Найти 5 пользователей с наибольшим количеством невозвращенных книг


qs = Member.objects.values('last_name', 'first_name').annotate(
    active_borrow_count=Count('borrows', filter=Q(borrows__is_borrowed=False))
).filter(active_borrow_count__gt=0).order_by('-active_borrow_count')[:5]

#print(qs.query)

"""SELECT `library_member`.`last_name` AS `last_name`, `library_member`.`first_name` AS `first_name`,
 COUNT(CASE WHEN `borrows`.`is_borrowed` = False THEN `borrows`.`id` ELSE NULL END) AS `active_borrow_count` FROM `library_member`
  LEFT OUTER JOIN `borrows` ON (`library_member`.`id` = `borrows`.`member_id`) GROUP BY 1,
 2 HAVING COUNT(CASE WHEN (`borrows`.`is_borrowed` = False) THEN `borrows`.`id` ELSE NULL END) > 0 ORDER BY 3 DESC LIMIT 5"""

"""Задача 10: Книги дороже средней цены в своем жанре**
# **ТЗ:** Найти книги, цена которых превышает среднюю цену книг в том же жанре"""

avg_prise = Book.objects.filter(category=OuterRef('category')).values('category').annotate(avg_price=Avg('price')).values('avg_price')
books = Book.objects.annotate(avg_price=Subquery(avg_prise)).filter(price__gt=F('avg_price'))

#print(books.query)
#for book in books:
#    print(f"{book.name} - {book.price} - {book.avg_price}")

""" Авторы с наибольшим количеством займов на книгу**
# **ТЗ:** Найти авторов, у которых среднее количество займов на книгу больше общего среднего по системе"""

#data = Author.objects.annotate(count_book=Count('books'), count_borrowed=Count("books__borrows")).filter(count_book__gt=0
#).annotate(avg_borrows_per_book=Cast(F("count_borrowed"), FloatField()) / Cast(F("count_book"), FloatField()))
#
#avg_total = data.aggregate(avg_sistem=Avg("avg_borrows_per_book"))["avg_sistem"]
#query6 = data.filter(avg_borrows_per_book__gt=avg_total).order_by('-avg_borrows_per_book')
#
#print(query6)
#
#for a in query6:
#    print(f"{a.name}, {a.avg_borrows_per_book}")






















from library.models import Author

from django.db.models import Avg, F, Count, FloatField
from django.db.models.functions import Cast

data = Author.objects.annotate(
    count_book=Count('books', distinct=True),
    count_borrowed=Count("books__borrows", distinct=True)).filter(
    count_book__gt=0
).annotate(
    avg_borrows_per_book=Cast(F("count_borrowed"), FloatField()) / Cast(F("count_book"), FloatField())
)


avg_total = data.aggregate(avg_sistem=Avg("avg_borrows_per_book"))["avg_sistem"]
query6 = data.filter(avg_borrows_per_book__gt=avg_total).order_by('-avg_borrows_per_book')

print(query6)

for a in query6:
    print(f"{a.name}, {a.avg_borrows_per_book}")
