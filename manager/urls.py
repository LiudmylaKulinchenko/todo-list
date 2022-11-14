from django.urls import path

from manager.views import TaskList, TagList

urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("tags/", TagList.as_view(), name="tag-list"),
]


app_name = "manager"
