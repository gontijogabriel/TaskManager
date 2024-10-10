import django_filters
from django import forms
from task.models import Task

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
