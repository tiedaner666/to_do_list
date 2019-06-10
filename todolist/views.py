from django.shortcuts import render


def home(request):
    content = {'待办事项': request.POST['待办事项']}
    return render(request, "todolist/home.html", content)


def about(request):
    return render(request, "todolist/about.html")


def edit(request):
    return render(request, "todolist/edit.html")
