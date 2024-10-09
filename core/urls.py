from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls')),
    path('', lambda request: redirect('task_list')),
    path('', include('task.urls')),
]
