from django.contrib import admin
from library.models import Author, Book
from library.models.publisher import Publisher


# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)


