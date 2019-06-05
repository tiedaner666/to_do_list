from django.shortcuts import render


def home(request):
    return render(request, "todolist/home.html")


def about(request):
    return render(request, "todolist/about.html")


def edit(request):
    return render(request, "todolist/edit.html")
