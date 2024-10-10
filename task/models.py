from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel

User = get_user_model()

class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class WorkTime(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField() 
    hours_worked = models.DurationField()
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Work Time"
        verbose_name_plural = "Work Times"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        self.hours_worked = self.end_time - self.start_time
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.hours_worked} horas trabalhadas em {self.created_at} - Task: {self.task.title}"