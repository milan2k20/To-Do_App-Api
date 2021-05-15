from rest_framework.viewsets import ModelViewSet
from ToDoApiSystem.models import ToDo
from ToDoApiSystem.Serializers import ToDoSerializer


class ToDoView(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
