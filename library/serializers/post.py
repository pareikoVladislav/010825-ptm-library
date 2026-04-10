from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from library.models import Posts


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Posts
        fields = [
            'id',
            'title',
            'published_date',
            'author',
        ]

class PostRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'


class PostCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Posts
        fields = [
            'title',
            'post_text',
            'author',
            'moderated',
            'library',
        ]

        extra_kwargs = {
            'title': {'required': False},
            'post_text': {'required': False},
            'author': {'required': False},
            'moderated': {'required': False},
            'library': {'required': False},
        }

        validators = []
