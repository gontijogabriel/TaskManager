from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, View
from django.shortcuts import get_object_or_404, redirect
from django_filters.views import FilterView

from task.models import Task, WorkTime
from task.forms import TaskForm, WorkTimeForm
from task.filters import TaskFilter


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    success_url = reverse_lazy('task_list')
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        filter_value = self.request.GET.get('filter', 'todos')

        if filter_value == 'pendentes':
            queryset = queryset.filter(status=False)
        elif filter_value == 'finalizados':
            queryset = queryset.filter(status=True)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks_count'] = Task.objects.all().count()
        context['pending_tasks_count'] = Task.objects.filter(status=False).count()
        context['completed_tasks_count'] = Task.objects.filter(status=True).count()

        filterset = self.get_filterset(self.filterset_class)
        context['filter'] = filterset

        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskCheck(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.user == request.user:
            task.status = True
            task.save()
        
        return redirect('task_list') 
        

class WorkTimeCreateView(LoginRequiredMixin, CreateView):
    model = WorkTime
    form_class = WorkTimeForm
    template_name = 'task_list.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        task_id = self.request.POST.get('task')
        task = get_object_or_404(Task, id=task_id)
        kwargs['task'] = task
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.task = form.cleaned_data['task']
        return super().form_valid(form)