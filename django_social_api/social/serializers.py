from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import User, Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            'id',
            'name',
            'login',
            'last_login',
            'last_request'
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=(
            ''
        )

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields=(
            'id',
            'user',
            'post',
            'date_added'
        )