from django.shortcuts import render, get_object_or_404
from .models import Task, Block
# from django.http import HttpResponse


def printing_message(request):
    tasks = Block.objects.all()
    content = {
        'tasks': tasks
    }
    return render(request, 'spravka/index.html', content)
