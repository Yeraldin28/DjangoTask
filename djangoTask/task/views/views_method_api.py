from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from task.models.request_task import RequestTask
from task.models.request_comment import TaskComment
from task.serializers.serializers import ProjectSerializer, CommentSerializer


@api_view(['GET', 'POST'])
def method_get_task(request):
    if request.method == 'GET':
        tasks= RequestTask.objects.all()
        serializer = ProjectSerializer(tasks)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            #convertir y guardar el modelo 
            task = Editorial(**validated_data)
            task.save()
            serializer_response = ProjectSerializer(task)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def method_GPD_task(request, pk):
    try: 
        task= RequestTask.objects.get(pk=pk)
    except RequestTask.DoesNotExist:
        return response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProjectSerializer(task)
        return Response(serializer.data)
    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        serializer =ProjectSerializer(task,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            # task = RequestTask(**serializer.validated_data)
            # task.pk = pk
            # task.save(update_fields=[name,description, status, priority, deadline])
            # task = RequestTask.objects.get(pk=pk)
            # serializer_response = ProjectSerializer(task)
            return Response(task.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#VISTAS BASADAS EN CLASES 

class TaskListApiView(APIView):
        def get(self, request):
            tasks= RequestTask.objects.all()
            serializer = ProjectSerializer(tasks, many=True)
            return Response(serializer.data)

        def post (self, request):
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
            #convertir y guardar el modelo 
                task = Editorial(**validated_data)
                task.save()
                serializer_response = ProjectSerializer(task)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
class TaskEditApiView(APIView):
    def get_object(self, pk):
        tasks = get_object_or_404(RequestTask, pk=pk)
        return tasks

    def get(self, request, pk):
        tasks = self.get_object(pk)
        serializer = ProjectSerializer(tasks)
        return Response(serializer.data)

    def delete(self, request, pk):
        tasks = self.get_object(pk)
        tasks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def PUT(self, request, pk):
        tasks = get_object_or_404(RequestTask, pk=pk)
        serializer =ProjectSerializer(tasks,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            # task = RequestTask(**serializer.validated_data)
            # task.pk = pk
            # task.save(update_fields=[name,description, status, priority, deadline])
            # task = RequestTask.objects.get(pk=pk)
            # serializer_response = ProjectSerializer(task)
            return Response(task.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
