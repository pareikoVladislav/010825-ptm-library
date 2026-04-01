from rest_framework import serializers

from library.models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'