'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BlockSerializer, TaskSerializer
from .models import Block, Task


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Block': '/block/',
        'List': '/task-list/',
        'Detail View': '/task-detail/<int:pk>/',
        'Create': '/task-create/',
        'Updete': '/task-update/<int:pk>/',
        'Delete': '/task-delete/<int:pk>/'
    }
    return Response(api_urls)


@api_view(['GET'])
def blockList(request):
    tasks = Block.objects.all()
    serializer = BlockSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request)
    print('дошел до проверки')

    if serializer.is_valid():
        print('проверка пройдена')
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task Deleted Successfully")
'''
