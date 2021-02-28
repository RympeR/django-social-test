from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import WorkoutSerializer, TroubleSerializer
from django.core.paginator import Paginator
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes, renderer_classes
import os
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer