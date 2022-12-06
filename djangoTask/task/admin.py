from django.contrib import admin
from .models import  TaskComment, Task

class TaskAdmin(admin.ModelAdmin):
    list_display= ('id', 'task_name', 'task_description', 'deadline')
    list_display_links = ('id', 'task_name')
    list_per_page = 1

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment)

