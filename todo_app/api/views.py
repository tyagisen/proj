from todo_app.api.serializers import TodoSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from todo_app.models import Todo
from todo_app.api.serializers import TodoSerializer

class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    search_field = ['title']


class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateAPIView(UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
