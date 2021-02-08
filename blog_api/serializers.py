from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('category', 'id', 'title', 'image', 'content', 'link', 'author')
        model = Post



