from rest_framework import generics
from rest_framework.authentication import BasicAuthentication

from library.models import Category
from library.serializers import CategorySerializer
 
 
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    authentication_classes = [BasicAuthentication]