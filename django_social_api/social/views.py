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
from .models import SocialUser, Post, Like
from django.db.models import Q


# class UserDetailView(generics.RetrieveAPIView):
#     queryset = SocialUser.objects.get()

class UserAPI(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)  
    def get(self, request, pk):
        user = SocialUser.objects.get(pk=pk)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
  

class UserAuthAPI(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)
    def get(self, request):
        user =  get_object_or_404(SocialUser,
            Q(login=request.data['login'])&
            Q(password=request.data['password'])
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
            return Response({
                "user": user.id
            })
        else:
            return Response(status=403)

class LikeCreateView(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)
    def post(self, request):
        print(request.data)
        like = LikeCreateSerializer(data=request.data)
        if like.is_valid():
            like.save()
            return Response({
                "like": like.id
            })
        else:
            return Response(status=400)

class PostCreateView(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)

    def post(self, request):
        data = request.data
        data['user'] = SocialUser.objects.get(
            pk=request.data['user_id']
        )
        del data['user_id']
        post = Post.objects.create(
            user=data['user'],
            name=data['name'],
            image=data['image'],
            description=data.get('desrciption', '')
        )
        post.save()
        return Response({
                "post": post.id
            })


class PostAPI(APIView):
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)
    
    def get(self, request, pk):
        post = PostSerializer.get(post_pk=pk)
        domain = request.get_host()
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
    renderer_classes=(JSONRenderer,)    
    permission_classes=(permissions.AllowAny, )
    parser_classes=(MultiPartParser,)
    serializer = LikeSerializer
    def get_queryset(self):
        likes = Like.objects.filter(added_date__gte=self.request.GET['begin_date'], added_date__lte=self.request.GET['end_date']).values('added_date').annotate(dcoun=Count('id'))
        return likes

