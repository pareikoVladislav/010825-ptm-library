from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from library.models import Author
from library.serializers.authors import AuthorSerializer
from library.filters.authors import AuthorFilter


class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter