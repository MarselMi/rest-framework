from authors.views import AuthorViewSet, BookModelViewSet, BiographyModelViewSet, ArticlesModelViewSet, AuthorView
from TODOapp.views import ProjectViewSet, TODOViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView


router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookModelViewSet)
router.register('biography', BiographyModelViewSet)
router.register('articles', ArticlesModelViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', TODOViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)

urlpatterns = [
    path('api/users/0.1', include('TODOapp.urls', namespace='0.1')),
    path('api/users/0.2', include('TODOapp.urls', namespace='0.2')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view/', AuthorView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
