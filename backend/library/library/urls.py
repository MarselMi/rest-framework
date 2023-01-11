from authors.views import AuthorModelViewSet, BookModelViewSet, BiographyModelViewSet, ArticlesModelViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
