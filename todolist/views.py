from django.shortcuts import render,redirect
from .models import todoapp
# Create your views here.

def home(request):
    data = todoapp.objects.all()
    return render (request, 'home.html', {'data': data})
 

def add(request):
    tododata = request.POST['todo']
    todo_item= todoapp(content=tododata)
    todo_item.save()
    return redirect(home)


def deleteItem(request, todo_id):
    item =todoapp.objects.get(id=todo_id)
    item.delete()
    return redirect(home)
     
    