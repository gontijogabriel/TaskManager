from django import forms

from task.models import Task, WorkTime


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título da tarefa'}),
            'description': forms.Textarea(attrs={'placeholder': 'Descrição da tarefa'}),
        }


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

        if start_time and end_time and end_time <= start_time:
            raise forms.ValidationError("A data e hora final devem ser posteriores à data e hora inicial.")

        return cleaned_data