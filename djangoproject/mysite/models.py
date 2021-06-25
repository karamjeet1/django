from django.db import models
from django.db.models import Model


class TodoList(models.Model):
    objects = None
    name = models.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return self.name


class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    completed = models.BooleanField()

    def __str__(self):
        return self.text
