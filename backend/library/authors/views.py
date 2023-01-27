from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Author, Biography, Book, Article
from .serializers import AuthorSerializer, BookSerializer, BiographySerializer, ArticleSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response


class AuthorView(APIView):
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
