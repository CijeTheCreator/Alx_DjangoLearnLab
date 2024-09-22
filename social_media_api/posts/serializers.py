from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    token = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at', 'token']
        read_only_fields = ['id', 'created_at', 'updated_at', 'token']

    def create(self, validated_data):
        # Create comment
        comment = Comment.objects.create(**validated_data)
        # Create token for the author
        token, _ = Token.objects.get_or_create(user=comment.author)
        comment.token = token.key
        return comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'token']
        read_only_fields = ['id', 'created_at', 'updated_at', 'comments', 'token']

    def create(self, validated_data):
        # Create post
        post = Post.objects.create(**validated_data)
        # Create token for the author
        token, _ = Token.objects.get_or_create(user=post.author)
        post.token = token.key
        return post
