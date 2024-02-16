from .import views
from django.urls import path
from todo_app.api.views import TodoListAPIView, TodoCreateAPIView



urlpatterns = [
    path('', TodoListAPIView.as_view(), name='todo-list'),
    path('todo_create/', TodoCreateAPIView.as_view(), name='todo-create')
]