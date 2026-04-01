from django.urls import path, include


urlpatterns = [
    path('categories/', include('library.urls.categories')),
]
