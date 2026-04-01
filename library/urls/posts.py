from library.views.posts import PostListView

from django.urls import path


urlpatterns = [
    path('posts/', PostListView.as_view(), name='list'),
]