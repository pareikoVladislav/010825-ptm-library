import django_filters

from library.models import Author

class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
    surname = django_filters.CharFilter(field_name='surname',lookup_expr='icontains')
    rating_min = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
    rating_max = django_filters.NumberFilter(field_name='rating', lookup_expr='lte')
    deleted = django_filters.BooleanFilter(field_name='deleted')
    
    class Meta:
        model = Author
        fields = ['name', 'surname', 'rating_min', 'rating_max', 'deleted']