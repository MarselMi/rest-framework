from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from TODOapp.models import User, Project, TODO
from .serializers import UserSerializer, ProjectSerializer, TODOSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action


class ProjectOffsetPaginator(LimitOffsetPagination):
    default_limit = 10


class ToDoOffsetPaginator(LimitOffsetPagination):
    default_limit = 20


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectOffsetPaginator

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name')
        if name:
            return Response(ProjectSerializer(self.queryset.filter(name=name), many=True).data)
        return Response(ProjectSerializer(self.queryset, many=True).data)

    @action(detail=False, methods=['GET'])
    def get_user(self, request):
        name = request.GET.get('name')
        if name:
            return Response(ProjectSerializer(self.queryset.filter(name=name), many=True).data)
        return Response([])


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.filter(status=True)
    serializer_class = TODOSerializer
    pagination_class = ToDoOffsetPaginator

    def list(self, request, *args, **kwargs):
        project_id = request.GET.get('project_id')
        if project_id:
            return Response(TODOSerializer(self.queryset.filter(project_id=project_id), many=True).data)
        return Response(TODOSerializer(self.queryset, many=True).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = False
        instance.save()
        return Response({"STATUS": "DELETED"})


class UserView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = User.objects.all()
        serializer = UserSerializer(articles, many=True)
        return Response(serializer.data)

