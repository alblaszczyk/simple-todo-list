from django import forms

from .models import ToDoList, Task

class ToDoListForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = '__all__'

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name',)
