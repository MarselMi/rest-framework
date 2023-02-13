from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Author, Biography, Book, Article
from .serializers import AuthorSerializer, BookSerializer, BiographySerializer, ArticleSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny


class AuthorView(APIView):
    permission_classes = AllowAny
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BiographyModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ArticlesModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
