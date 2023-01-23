from rest_framework.viewsets import ModelViewSet
from TODOapp.models import User, Project, TODO
from .serializers import UserSerializer, ProjectSerializer, TODOSerializer
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class UserViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TODOViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
