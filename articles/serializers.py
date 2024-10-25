from rest_framework import serializers
from .models import Article, Topic
from django.contrib.auth.models import User

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'thumbnail', 'topics']
    
    def create(self, validated_data):
        # Moderatsiya uchun maqolani yaratish, ammo ko'rinmasdan
        validated_data['status'] = 'pending'
        return super().create(validated_data)

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    topics = TopicSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'summary', 'content', 'status', 'thumbnail', 'created_at', 'updated_at', 'topics']
