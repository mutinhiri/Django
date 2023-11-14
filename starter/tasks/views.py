from django.shortcuts import render
from django import forms 

tasks = ['foo', 'bar', 'baz']


class NewTaskForm(forms.Form):
    task = forms.CharField(label="Newt Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        'tasks': tasks
    })


def add(request):
    # return render(request, 'tasks/add.html')
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })