import django
from django.db import models
from django.utils import timezone

class Board(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(default=timezone.now())

class TaskList(models.Model):
  name = models.CharField(max_length=50)
  created_at = models.DateTimeField(default=timezone.now())
  board = models.ForeignKey(Board, on_delete = models.CASCADE)

  def __str__(self):
    return f"{self.name}"

  
CHOICES = (
        ('P', 'PENDING'),
        ('C', 'COMPLETED'),
        ('IP', 'IN_PROGRESS'),
        ('D', 'DROPPED')
    )

class Task(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  created_at = models.DateTimeField(default=timezone.now())
  due_date = models.DateTimeField()
  list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
                                                          

  def __str__(self):
    return f"{self.name}"