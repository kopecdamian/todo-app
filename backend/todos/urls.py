from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_tasks, name='all_tasks'),
    path('task_create', views.task_create, name='task_create'),
    path('<int:task_id>', views.task_details, name='task_details'),
]