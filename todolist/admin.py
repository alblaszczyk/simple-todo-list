from django.contrib import admin
from .models import ToDoList, Task


admin.site.register(ToDoList, admin.ModelAdmin)
admin.site.register(Task, admin.ModelAdmin)
