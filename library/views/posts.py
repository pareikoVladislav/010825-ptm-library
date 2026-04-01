from rest_framework.generics import ListAPIView

from library.models import Posts
from library.serializers.posts import PostSerializer


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        queryset = Posts.objects.all()
        
        author_id = self.request.query_params.get('author_id')
        moderated = self.request.query_params.get('moderated')
        
        if author_id:
            queryset = queryset.filter(author_id=author_id)
            
        if moderated is not None:
            moderated_value = moderated.lower() == 'true'
            queryset = queryset.filter(moderated=moderated_value)
            
        return queryset