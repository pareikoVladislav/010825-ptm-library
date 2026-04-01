from django.urls import path, include


urlpatterns = [
    path('categories/', include('library.urls.categories')),
    path('posts/', include('library.urls.posts')),
    path('books/', include('library.urls.books')),
    # path('books/', include('library.urls.books')),
    path('authors/', include('library.urls.authors')),
]
