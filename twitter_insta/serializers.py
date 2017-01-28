from rest_framework import serializers

from models import Post, Hashtag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_name', 'known_user', 'content', 'lat', 'lon', 'profile_pic', 'content_date', 'source_type', 'has_location', 'thumbnail_link', 'image_link', 'display_name')

class HashtagStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('hashtag', 'verified_count', 'unverified_count')