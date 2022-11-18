from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from blog.models import Blog


class BLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields= ('title','subtitle', 'author')