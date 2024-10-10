from django.urls import path
from task.views import TaskListView, TaskCreateView, WorkTimeCreateView, TaskCheck

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('task/check/<int:pk>/', TaskCheck.as_view(), name='task_check'),
    path('worktime/create/', WorkTimeCreateView.as_view(), name='worktime_create'),
]