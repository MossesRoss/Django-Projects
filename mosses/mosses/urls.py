from django.contrib import admin
from django.urls import path, include
from mosapp.views import TaskListCreateView, TaskDetailView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mosapp.urls')),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('', home, name='home'),
]
