from django.http import HttpResponseRedirect
from django.shortcuts import render
from mysite.models import TodoList
from .forms import CreateNewList


# Create your views here.

def index(response, id):
    ls = TodoList.objects.get(id=id)
    return render(response, 'list.html', {"ls": ls})


def home(response):
    return render(response, 'home.html', {})


def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = TodoList(name=n)
            t.save()
        return HttpResponseRedirect("/%n" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'create.html', {"form": form})
