from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorSerializer, BookSerializer, BiographySerializer, ArticleSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class AuthorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = BookSerializer


class BiographyModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = BiographySerializer


class ArticlesModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = ArticleSerializer
