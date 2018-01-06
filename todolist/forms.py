from django import forms
from django.contrib.auth.models import User
from .models import ToDoList, Task

class ToDoListForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = '__all__'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name',)

    
