from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    tasks = Task.objects.all()
    context = {'form':form,'tasks':tasks}
    return render(request,'todo/index.html',context)

def delete_view(request,id):
    tasks =Task.objects.get(id=id)
    tasks.delete()
    return redirect('/')

def item_view(request,id):
    tasks =Task.objects.get(id=id)
    return render(request,'todo/item.html',{'tasks':tasks})
    
