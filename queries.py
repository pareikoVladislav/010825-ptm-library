import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django.setup()

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
