from django.db import models

class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.name)

class Task(models.Model):
    todo_list = models.ForeignKey('todolist.ToDoList', on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    task_done = models.BooleanField(default=False)

    def done(self):
        self.task_done = True
        self.save()

    def __str__(self):
        return '%s %s' % (self.todo_list, self.name)
