from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import(
    UserSerializer, 
    LikeSerializer, 
    PostSerializer, 
    UserCreateSerializer,
    PostCreateSerializer,
    LikeCreateSerializer
)
from django.shortcuts import get_object_or_404    
from django.core.paginator import Paginator
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
import os
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import generics
from .models import User, Post, Like



class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.get()

class UserAPI(APIView):
    permission_classes=(permissions.AllowAny, )
    renderer_classes=(JSONRenderer,)    
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
  

class UserAuthAPI(APIView):
    def get(self):
        user = get_object_or_404(User,
            login=self.request.data['login'],
            password=self.request.data['password']
        )
        if user:
            user.save() 
            return Response({
                "id": user.id,
                "auth_token": 'test',
            })
        else:
            return Response(
                {
                    "status": "invalid creds"
                }
            ) 

    def post(self, request):
        user =UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
        return Response(status=201)

class LikeCreateView(APIView):
    def post(self, request):
        like = LikeCreateSerializer(data=request.data)
        if like.is_valid():
            like.save()
            return Response(status=201)
        else:
            return Response(status=400)
class PostCreateView(APIView):
    def post(self, request):
        post = PostCreateSerializer(data=request.data)
        if post.is_valid():
            post.save()
        return Response(status=201)

class LikeAPI(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    
    def put(self):
        like = Like.objects.get(pk=self.request.GET['like_id'])    
        like.liked = self.request.data['liked']
        like.save()

class PostAPI(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)
    
    def get(self):
        post = PostSerializer.get(self.request.GET['post_pk'])
        domain = self.request.get_host()
        path_image = post.image.url
        image_url = 'http://{domain}{path}'.format(
            domain=domain, path=path_image)
        return Response(
            {
                "id": post.id,
                "name": post.name,
                "image": image_url,
                "description": post.description
            }
        )
    
class Analytics(generics.ListAPIView):
    serializer = LikeSerializer
    def get_queryset(self):
        likes = Like.objects.filter(added_date__gte=self.request.GET['begin_date'], added_date__lte=self.request.GET['end_date']).values('added_date').annotate(dcoun=Count('id'))
        return likes

