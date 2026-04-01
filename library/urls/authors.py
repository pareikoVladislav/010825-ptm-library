from library.views.authors import AuthorList

from django.urls import path


urlpatterns = [
    path('', AuthorList.as_view())
]