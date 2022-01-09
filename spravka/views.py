from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse


def printing_message(request):
    title = 'список'
    message = 'Hello world!'
    content = {
        'title': title,
        'message': message
    }
    return render(request, 'spravka/index.html', content)
