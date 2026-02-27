from django.db import models
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator

       
class Member(models.Model):
    first_name:str = models.CharField(max_length=50, verbose_name="Имя") 
    last_name:str = models.CharField(max_length=50, verbose_name="Фамилия") 
    email:str = models.EmailField(unique=True)
    gender:str = models.CharField(
        max_length=20,
        choices=[
            ('male','Мужской'),
            ('female','Женский'),
            ('other','Другой')
        ],
        verbose_name="Пол"
    )
    birth_date:date = models.DateField(verbose_name="Дата рождения")
    age:int = models.IntegerField(
        validators=[
            MinValueValidator(6),
            MaxValueValidator(120)
        ],
        verbose_name="Возраст"
    )
    role:str = models.CharField(
        max_length=20,
        choices=[
            ('admin','Админ'),
            ('staff','Сотрудник'),
            ('member','Читатель')
        ],
        verbose_name="Роль"
    )
    
    is_active:bool = models.BooleanField(default=True, verbose_name="Активный")
    
    libraries: "Library"= models.ManyToManyField("Library", verbose_name="Библиотеки")
    
    



# class Membership(models.Model):
#     member: 'Member' = models.ForeignKey(to='Member', on_delete=models.CASCADE)
#     library: 'Library' = models.ForeignKey(to='Library', on_delete=models.CASCADE)
    
#     class Meta:
#         unique_together = ('member','library')
    
   