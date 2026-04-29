from django.shortcuts import render, redirect
from .models import Todos

# Create your views here.
def todos(request):
    if request.method == "POST":
        data = request.POST
        todo_name = data.get("todo_name")
        todo_desc = data.get("todo_desc")

        Todos.objects.create(
            todo_name = todo_name,
            todo_description = todo_desc
        )
        return redirect("todos")

    all_todos = Todos.objects.all()
    return render(request, "home.html", {"todos" : all_todos})

def delete_todo(request, id):
    query_set = Todos.objects.get(id=id)
    query_set.delete()
    return redirect("todos")

def update_todo(request, id):
    query_set = Todos.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        updated_name = data.get("todo_name")
        updated_desc = data.get("todo_desc")

        query_set.todo_name = updated_name
        query_set.todo_description = updated_desc

        query_set.save()

        return redirect("todos")

    return render(request, "update_todo.html", {"todo": query_set})