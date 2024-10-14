from django.contrib import admin

from task.models import Task, WorkTime


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at', 'user')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'title', 'description', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(WorkTime)
class WorkTimeAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'start_time', 'end_time', 'hours_worked', 'created_at')
    list_filter = ('start_time', 'end_time', 'created_at', 'user')
    search_fields = ('task__title', 'user__username', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('hours_worked', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'task', 'start_time', 'end_time', 'description')
        }),
        ('Calculations', {
            'fields': ('hours_worked',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
