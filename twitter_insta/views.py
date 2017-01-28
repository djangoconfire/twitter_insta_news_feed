from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from models import Hashtag, Post
from serializers import PostSerializer, HashtagStatSerializer, MemberStatSerializer
from django.shortcuts import render
import django_filters

class PostList(generics.ListAPIView):
    queryset = Post.objects.exclude(content__exact='').order_by('id')
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListRecent(generics.ListAPIView):
    queryset = Post.objects.exclude(content__exact='').order_by('-id')[:10]
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListTweet(generics.ListAPIView):
    queryset = Post.objects.exclude(content__exact='').filter(source_type='TW').order_by('-id')[:10]
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListInsta(generics.ListAPIView):
    queryset = Post.objects.exclude(content__exact='').filter(source_type='IN').order_by('-id')[:10]
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class PostListLocation(generics.ListAPIView):
    queryset = Post.objects.exclude(content__exact='').filter(known_user=True).filter(has_location=True)
    serializer_class = PostSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class MemberStatsList(generics.ListAPIView):
    queryset = Verified.objects.all()
    serializer_class = MemberStatSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class HashtagStatsList(generics.ListAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagStatSerializer
    permission_classes = [
        permissions.AllowAny
    ]

def index(request):
    return render(request, 'polls/index.html')
