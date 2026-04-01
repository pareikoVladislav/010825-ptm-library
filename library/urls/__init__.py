from django.urls import path, include


urlpatterns = [
    path('categories/', include('library.urls.categories')),
    path('posts/', include('library.urls.posts'))
]
