from rest_framework import serializers
from .models import User, Project, TODO


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'surname')


class UserSerializerWithFullName(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
