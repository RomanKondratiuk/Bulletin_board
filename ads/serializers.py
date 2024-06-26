from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Comment, Ad


class CommentSerializer(serializers.ModelSerializer):
    """ Used to view comments """
    class Meta:
        model = Comment
        fields = ('text', 'author', 'ad')


class AdSerializer(serializers.ModelSerializer):
    """ Used for listing ads, includes basic fields """

    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'description', "author")


class AdDetailSerializer(serializers.ModelSerializer):
    """ Used for detailed ad view, includes all fields and detailed information """
    author_details = UserSerializer(source='author', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
