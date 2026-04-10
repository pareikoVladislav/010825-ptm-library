from rest_framework import viewsets

from library.models import Posts
from library.serializers import PostCreateUpdateSerializer, PostSerializer, PostRetrieveSerializer


class PostViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return PostSerializer
        elif self.action == 'retrieve':
            return PostRetrieveSerializer
        # elif self.action in ('create', 'update', 'partial_update'):

        return PostCreateUpdateSerializer

    def get_queryset(self):
        posts = Posts.objects.all()

        moderated = self.request.query_params.get('moderated')
        if moderated:
            if moderated == 'true':
                posts = posts.filter(moderated=True)
            elif moderated == 'false':
                posts = posts.filter(moderated=False)
            else:
                posts = posts.none()

        return posts
    #
    # def partial_update(self, request, *args, **kwargs):
    #     print('*' * 50)
    #     print(self.get_serializer())
    #     print('*' * 50)
    #     return super().partial_update(request, *args, **kwargs)
