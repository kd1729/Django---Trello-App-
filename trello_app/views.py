from django.shortcuts import render, redirect
from .models import Task, TaskList, Board
from .forms import TaskListForm, TaskForm, BoardForm



def index(request):
  boards = Board.objects.all()
  return render(request, 'trello_app/index.html', {'boards': boards})
  

def add_task_list_form(request, board_id):
  if request.method == 'POST':
    form = TaskListForm(data=request.POST)
    name = request.POST['name']
    if form.is_valid():
      form.save()
      return redirect('display_board', board_id)
  else:
    form = TaskListForm(initial={'board': board_id})
  return render(request, 'trello_app/forms/new_list.html', {'form': form})


def add_task_form(request, list_id):
  if request.method == 'POST':
    form = TaskForm(data=request.POST)
    if form.is_valid():
      new_task = form.save()
      return redirect('display_list', list_id)
  else:
    form = TaskForm(initial={'list': list_id})
  return render(request, 'trello_app/forms/new_task.html', {'form': form})

def add_board(request):
  # TODO: Complete this method to create form object using BoardForm
  if request.method == 'POST':
    # TODO: extract form data from request in form object
    form = BoardForm(data = request.POST)

    if form.is_valid():
      # TODO: Save the form and redirect to index
      form.save()
      return redirect('/')

      # Remove this pass statement when done
     
  else:
    form = BoardForm()
  return render(request, 'trello_app/forms/new_board.html', {'form': form})


def show_board(request, id):
  # id is the board_id
  boards = Board.objects.filter(id=id)
  lists = TaskList.objects.filter(board=id)
  return render(request, 'trello_app/board.html', {'lists': lists, 'board_name': boards[0].name, 'board_id': boards[0].id})


def show_list(request, id):
  # id is the list_id
  lists = TaskList.objects.filter(id=id)
  tasks = Task.objects.filter(list=id)
  return render(request, 'trello_app/list.html', {'tasks': tasks, 'list_name': lists[0].name, 'list_id': lists[0].id})