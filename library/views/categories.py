from rest_framework import generics

from library.models import Category
from library.serializers import CategorySerializer

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

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()