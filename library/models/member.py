from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from library.models.library import Library

       
class Member(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True)
    gender = models.CharField(
        max_length=20,
        choices=[
            ('male','Мужской'),
            ('female','Женский'),
            ('other','Другой')
        ],
        verbose_name="Пол"
    )
    birth_date = models.DateField(verbose_name="Дата рождения")
    age = models.IntegerField(
        validators=[
            MinValueValidator(6),
            MaxValueValidator(120)
        ],
        verbose_name="Возраст"
    )
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin','Админ'),
            ('staff','Сотрудник'),
            ('member','Читатель')
        ],
        verbose_name="Роль"
    )
    
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    
    libraries = models.ManyToManyField(
        Library,
        through="Membership",
        verbose_name="Библиотеки",
        related_name="members"
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class Membership(models.Model):
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="membership_records"
    )
    library = models.ForeignKey(
        to=Library,
        on_delete=models.CASCADE,
        related_name="membership_records"
    )
    joined_at = models.DateField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('member','library')

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} - {self.library.name}"
