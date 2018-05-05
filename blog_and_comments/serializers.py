from django.contrib.auth.models import User
from registration.models import Custom_User
from .models import Blog
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class Custom_UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Custom_User
        fields = ('user', 'mobile', 'primary_registration_type')

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('url', 'title', 'blogger', 'image', 'content', 'draft', 'likes')