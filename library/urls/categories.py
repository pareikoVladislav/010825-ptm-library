from library.views.categories import CategoryListCreateAPIView
from django.urls import path


urlpatterns = [
    path('', CategoryListCreateAPIView.as_view())
]

