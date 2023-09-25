from django.db import models
from django.utils import timezone


class ToDoItem(models.Model):
    """this class defines a model for to do list where each to do item contains
    a text description of the task and due date."""
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.text}: due {self.due_date}"
