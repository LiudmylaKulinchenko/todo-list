from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskCreationForm, TaskUpdatingForm
from manager.models import Task, Tag


class TaskList(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 3


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("manager:task-list")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskUpdatingForm
    success_url = reverse_lazy("manager:task-list")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


class TagList(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreate(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("manager:tag-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("manager:tag-list")


class TagDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("manager:tag-list")


def task_status_update(request, pk: int):
    task = Task.objects.get(pk=pk)

    if task.is_done:
        task.is_done = False
    else:
        task.is_done = True

    task.save()

    return HttpResponseRedirect(reverse_lazy("manager:task-list"))
