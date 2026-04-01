"""## Задание 1. Category: список и создание через GenericAPIView + mixins
### Эндпоинты:
- `GET /api/v1/categories/`
- `POST /api/v1/categories/`
### Требования
- Использовать `GenericAPIView` с миксинами `ListModelMixin` и `CreateModelMixin`.
- Написать сериализатор `CategorySerializer` с полем `name`.
### Проверки
- `GET` возвращает список всех категорий (200).
- `POST` с валидными данными создаёт категорию (201).
- `POST` с дублирующимся `name` возвращает ошибку валидации (400), т.к. поле `unique=True`."""
from rest_framework import serializers
from library.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'