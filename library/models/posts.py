from django.db import models

from library.models import Library

from library.models import Member

from datetime import date

class Posts(models.Model):
    title: str = models.CharField(max_length=255, unique_for_date="published_date", verbose_name="Title_of_post")

    post_text: str = models.TextField()

    author: str = models.ForeignKey(Member,on_delete=models.CASCADE)

    moderated: bool = models.BooleanField(default=False)

    library: str = models.ForeignKey(Library,on_delete=models.CASCADE)

    published_date: date = models.DateField(auto_now_add=True)

    updated_date: date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
