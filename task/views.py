from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, View, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django_filters.views import FilterView
from django.http import JsonResponse

from task.models import Task, WorkTime
from task.forms import TaskForm, WorkTimeForm
from task.filters import TaskFilter, WorkTimeFilter

from datetime import timedelta

import json

User = get_user_model()


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'task/task_list.html'
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
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form)) 


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/task_edit.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class TaskCheck(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.user == request.user:
            task.status = True
            task.save()
        return redirect('task_list')


class WorkTimeListView(LoginRequiredMixin, FilterView):
    model = WorkTime
    template_name = 'task/worktime_list.html'
    context_object_name = 'worktimes'
    filterset_class = WorkTimeFilter
    success_url = reverse_lazy('worktime_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        start_time = self.request.GET.get('start_time')
        end_time = self.request.GET.get('end_time')
        hours_worked = self.request.GET.get('hours_worked')
        description = self.request.GET.get('description')
        task_id = self.request.GET.get('task')
        username = self.request.GET.get('user')

        if start_time:
            queryset = queryset.filter(start_time__gte=start_time)

        if end_time:
            queryset = queryset.filter(end_time__lte=end_time)

        if hours_worked:
            try:
                hours_worked_duration = self.parse_hours_worked(hours_worked)
                queryset = queryset.filter(hours_worked__gte=hours_worked_duration)
            except ValueError:
                pass

        if description:
            queryset = queryset.filter(description__icontains=description)

        if task_id:
            queryset = queryset.filter(task_id=task_id)

        if username:
            try:
                user = User.objects.get(username=username)
                queryset = queryset.filter(user_id=user.id)
            except User.DoesNotExist:
                pass

        return queryset

    def parse_hours_worked(self, hours_worked_str):
        hours, minutes = map(int, hours_worked_str.split(':'))
        return timedelta(hours=hours, minutes=minutes)


class WorkTimeCreateView(View):
    def post(self, request, *args, **kwargs):
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            form = WorkTimeForm(data)
        else:
            form = WorkTimeForm(request.POST)

        if form.is_valid():
            worktime = form.save(commit=False)
            worktime.user = request.user
            worktime.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    