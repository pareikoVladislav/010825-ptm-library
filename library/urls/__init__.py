from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views.posts import PostViewSet


default_router = DefaultRouter()
default_router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('categories/', include('library.urls.categories')),
    path('books/', include('library.urls.books')),
]

urlpatterns += default_router.urls