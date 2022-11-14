from django.shortcuts import render
from django.views import generic

from manager.models import Task, Tag


class TaskList(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 3


class TagList(generic.ListView):
    model = Tag
    paginate_by = 5
