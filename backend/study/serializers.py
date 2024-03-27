from rest_framework import serializers

from .models import Article, Section


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'text', 'updated', 'user')


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name', 'summary')


class SectionSerializer(serializers.ModelSerializer):
    articles = ArticleListSerializer(many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'articles')
