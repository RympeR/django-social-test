from django.urls import path
from .views import *

urlpatterns = [
    path('user/signup/', UserAuthAPI.as_view(), name='signUp'),
    path('user/get-profile/<int:pk>', UserAPI.as_view(), name='GetProfile'),
    path('user/login/', UserAuthAPI.as_view(), name='login'),
    path('analytics/', Analytics.as_view(), name='analytics'),
    path('like/', LikeCreateView.as_view(), name='like'),
    path('like/status/', LikeAPI.as_view(), name='LikeAPI'),
    
]
