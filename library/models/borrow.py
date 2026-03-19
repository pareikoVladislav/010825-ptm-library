from datetime import datetime

from django.db import models


class Borrow(models.Model):
    member = models.ForeignKey(
        "Member",
        verbose_name='Участник',
        on_delete=models.PROTECT,
        related_name='borrows',
    )

    book = models.ForeignKey(
        "Book",
        verbose_name='Книга',
        on_delete=models.PROTECT,
        related_name='borrows',
    )

    library = models.ForeignKey(
        "Library",
        verbose_name='Библиотека',
        on_delete=models.PROTECT,
        related_name='borrows',
    )

    start_date = models.DateField(
        verbose_name='Дата выдачи',
        auto_now_add=True,
    )

    end_plane_date = models.DateField(
        verbose_name='Планируемая дата возврата',
    )

    end_fact_date = models.DateField(
        verbose_name='Фактическая дата возврата',
        null=True,
        blank=True,
    )

    is_borrowed = models.BooleanField(
        verbose_name='Книгу вернули',
        default=False
    )

    class Meta:
        db_table = "borrows"

        verbose_name = 'Выдача книги'
        verbose_name_plural = 'Выдачи книг'
        ordering = ['-start_date']


    def __str__(self):

        return f"{self.member} -> {self.book}: {self.library}"


    def check_date_is_borrowed(self):
        if self.is_borrowed and self.end_plane_date < datetime.now():
            return False
        return True
