from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import SocialUser, Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=SocialUser
        fields='__all__'

class PostSerializer(serializers.ModelSerializer):

    SocialUser = serializers.SlugRelatedField(slug_field="login", read_only=True)
    class Meta:
        model=Post
        fields='__all__'

    @staticmethod
    def get(post_pk):
        post = Post.objects.get(pk=post_pk)
        print(post)
        return post

class LikeSerializer(serializers.ModelSerializer):

    SocialUser = serializers.SlugRelatedField(slug_field="login", read_only=True)
    post = serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model=Like
        fields='__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=SocialUser
        fields=(
            'name', 
            'login',
            'password'
        )

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=(
            'user',
            'image',
            'name',
            'description'
        )
    
class LikeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields=(
            'user',
            'post',
            'liked'
        )

    def create(self, validated_data):
        print(validated_data)
        like = Like.objects.update_or_create(
            user=validated_data.get('user', None),
            post=validated_data.get('post', None),
            defaults={"liked":validated_data.get('liked')}
        )
        return like

