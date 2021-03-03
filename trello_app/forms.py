from django import forms
from trello_app.models import Task, TaskList, Board

class TaskListForm(forms.ModelForm):
  class Meta:
    model = TaskList
    fields = ['name','board']

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['name', 'desc', 'due_date', 'list']
    widgets = {
      'due_date': forms.DateTimeInput(attrs= {'type': 'datetime-local'})
    }

class BoardForm(forms.ModelForm):
  class Meta:
    model = Board
    fields = ['name']
    
  