from django.contrib import admin
from library.models import Author, Book, Library
from library.models import Borrow
from library.models.publisher import Publisher


# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Library)



@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = [
        'member',
        'book',
        'library',
        'start_date',
        'end_plane_date',
        'end_fact_date',
        'is_borrowed',
    ]

    list_filter = [
        'is_borrowed',
        'member',
        'library',
    ]

    search_fields = ['book']

    list_editable = ('is_borrowed', 'end_plane_date')

    list_per_page = 25


