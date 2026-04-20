from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views.event import EventViewSet
from library.views.posts import PostViewSet


default_router = DefaultRouter()
default_router.register('posts', PostViewSet, basename='posts')
default_router.register('events', EventViewSet, basename='events')


urlpatterns = [
    path('categories/', include('library.urls.categories')),
    path('books/', include('library.urls.books')),
]

urlpatterns += default_router.urls