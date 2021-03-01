from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import User, Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="login", read_only=True)
    class Meta:
        model=Post
        fields='__all__'

    @staticmethod
    def get(self, post_pk):
        post = Post.objects.get(pk=post_pk)
        return post

class LikeSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field="login", read_only=True)
    post = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model=Like
        fields='__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields='__all__'

    def create(self, validated_data):
        post = Post.objects.get(pk=validated_data.get('id_post', None))
        user = User.objects.get(pk=validated_data.get('id_user', None))
        like = Like.objects.update_or_create(
            user=user,
            post=post,
            defaults={'liked':validated_data.get('liked') }
        )
        return like