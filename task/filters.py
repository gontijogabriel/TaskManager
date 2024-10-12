import django_filters
from django import forms
from task.models import Task, WorkTime

class TaskFilter(django_filters.FilterSet):

    user = django_filters.CharFilter(
        field_name='user__username',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome do usuário...'
        })
    )
    task = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Título da task...'
        })
    )
    start_time = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Data de início',
            'type': 'date'
        })
    )
    end_time = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Data de fim',
            'type': 'date'
        })
    )
    description = django_filters.CharFilter(
        field_name='description',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Descrição...'
        })
    )
    
    class Meta:
        model = Task
        fields = ['user', 'task', 'start_time', 'end_time', 'description']


class WorkTimeFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter(
        field_name="start_time",
        lookup_expr='gte',
        label="Data de Início (>=)",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Data de Início',
            'type': 'datetime-local'
        })
    )
    end_time = django_filters.DateTimeFilter(
        field_name="end_time",
        lookup_expr='lte',
        label="Data de Término (<=)",
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Data de Término',
            'type': 'datetime-local'
        })
    )
    hours_worked = django_filters.DurationFilter(
        field_name="hours_worked",
        label="Horas Trabalhadas",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Horas Trabalhadas (HH:MM)'
        })
    )
    description = django_filters.CharFilter(
        field_name="description",
        lookup_expr='icontains',
        label="Descrição",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Descrição...'
        })
    )
    task = django_filters.CharFilter(
        field_name="task__title",
        lookup_expr='icontains',
        label="Título da Tarefa",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Título da Tarefa...'
        })
    )
    user = django_filters.CharFilter(
        field_name="user__username",
        lookup_expr='icontains',
        label="Usuário",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome do Usuário...'
        })
    )

    class Meta:
        model = WorkTime
        fields = ['start_time', 'end_time', 'hours_worked', 'description', 'task', 'user']