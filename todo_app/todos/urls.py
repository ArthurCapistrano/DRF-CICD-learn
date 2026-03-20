from django.urls import path
from .views import TaskCreateListView, TaskListView, TaskDeleteView

urlpatterns = [
    path('tasks/', TaskCreateListView.as_view(), name='task-list-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]