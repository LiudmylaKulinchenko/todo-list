from django.urls import path

from manager.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
]


app_name = "manager"
