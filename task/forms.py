from django import forms

from task.models import Task, WorkTime

from django.utils import timezone


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Título'})
    )
    description = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Descrição'})
    )

    class Meta:
        model = Task
        fields = ['title', 'description']

        
class WorkTimeForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Data e Hora de Início"
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Data e Hora de Fim"
    )

    class Meta:
        model = WorkTime
        fields = ['task', 'start_time', 'end_time', 'description']
        widgets = {
            'task': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descrição do trabalho realizado'}),
        }


    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        data_atual = timezone.now()

        if not start_time or not end_time:
            raise forms.ValidationError("Os campos de horário de início e fim são obrigatórios.")

        if start_time >= end_time:
            raise forms.ValidationError("O horário de início deve ser anterior ao horário de fim.")

        if end_time > data_atual:
            raise forms.ValidationError("Horário final inválido, deve ser anterior ao horário atual.")

        return cleaned_data