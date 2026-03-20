from django.urls import path
from .views import TaskCreateListView, TaskDeleteView

urlpatterns = [
    path('tasks/', TaskCreateListView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]