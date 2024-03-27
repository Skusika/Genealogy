from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Article, Section
from .serializers import ArticleSerializer, SectionSerializer


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.visible.all()
    serializer_class = ArticleSerializer


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    articles = Article.visible.all()

    # Объект Prefetch позволяет передать в prefetch_related только статьи с is_visible == True
    queryset = Section.visible.all().prefetch_related(Prefetch('articles', queryset=articles))
    serializer_class = SectionSerializer
