from django import forms
from task.models import Task, WorkTime


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
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

    def __init__(self, *args, **kwargs):
        self.task = kwargs.pop('task', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if self.task:
            if start_time and start_time < self.task.created_at:
                self.add_error('start_time', 'O início do trabalho não pode ser anterior à data de criação da tarefa.')
            if end_time and end_time < start_time:
                self.add_error('end_time', 'O término do trabalho não pode ser anterior ao início.')

        return cleaned_data