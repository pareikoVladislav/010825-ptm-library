"""
Задание 1. список пользователей доступен только администраторам
Эндпоинты:
Требования
Реализовать custom permission, который:
Разрешает доступ только администраторам.
Для всех остальных аутентифицированных пользователей возвращает 403.
Подключить permission к эндпоинтам списка и детализации пользователей.
Для анонимного пользователя возвращать 401.

"""

from rest_framework.permissions import BasePermission


class IsAdminOnly(BasePermission):

    def has_permission(self, request, view):
        #if request.user.role == 'admin':
        #     return True
        # return False
        print(request.user)
        return request.user and request.user.is_authenticated and request.user.role == 'admin'


    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'
