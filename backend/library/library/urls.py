from authors.views import AuthorViewSet, BookModelViewSet, BiographyModelViewSet, ArticlesModelViewSet, AuthorView
from TODOapp.views import UserViewSet, ProjectViewSet, TODOViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('articles', ArticlesModelViewSet)
router.register('users', UserViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', TODOViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view/', AuthorView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]
