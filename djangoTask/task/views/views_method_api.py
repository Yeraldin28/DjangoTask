from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from task.models.request_task import RequestTask
from task.models.request_comment import TaskComment
from task.serializers.serializers import ProjectSerializer, CommentSerializer

#VISTAS BASADAS EN FUNCIONES 

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
                task = RequestTask(**validated_data)
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


#Vistas Genericas con mixins
class TaskListGenericApiView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
        queryset = RequestTask.objects.all()
        serializer_class = ProjectSerializer
        def get(seft, request, *args, **kwargs):
            return seft.list(request, *args, **kwargs)

        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
        
        
class TaskEditGenericApiView(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = RequestTask.objects.all()
    serializer_class = ProjectSerializer
    
    def perform_destroy(self, instance):
        instance.status = 'DONE'
        instance.save()
    
    def get(seft, request, *args, **kwargs):
            return seft.retrieve(request, *args, **kwargs)
        
    def delete(seft, request, *args, **kwargs):
            return seft.destroy(request, *args, **kwargs)
        
    def put(seft, request, *args, **kwargs):
            return seft.update(request, *args, **kwargs)

# Vistas Concretas
class TaskListConcretaGenericApiView(generics.ListAPIView, generics.CreateAPIView):
        queryset = RequestTask.objects.all()
        serializer_class = ProjectSerializer

# Paginacion de paginas
# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000



#Vista de conjunto

class TaskViewSet(viewsets.ViewSet):
        def list(self, request):
            queryset = RequestTask.objects.all()
            serializer = ProjectSerializer(queryset, many=True)
            return Response(serializer.data)

        def retrieve (self, request, pk=None):
            queryset = RequestTask.objects.all()
            user = get_object_or_404(queryset, pk=pk)
            serializer = ProjectSerializer(user)
            return Response(serializer.data)
        
        
 #VISTAS EN MODELOS           
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = RequestTask.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    
class ProjectViewSetLook(viewsets.ReadOnlyModelViewSet):
    queryset = RequestTask.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    
    
#MIXINS PERSONALIZADO

# class ListTaskModelMixin:
#     """
#     List a queryset.
#     """
#     def list(self, request, *args, **kwargs):
#         filtro = {}
        
#         if("buscar" in self.request.query_params):
#             valor = self.request.query_params['buscar']
#             campo = self.busqueda_id if valor.is_numeric() else f'{self.budqueda_str}__contains'
#             filtro[campo] = valor
            
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


#FILTRADO POR AGRUPACION 

from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

class TaskFilter(filters.FilterSet):
    filterName = filters.CharFilter(
        field_name='name',
        lookup_expr='exact',
        label='name'
    )
    filterDate = filters.DateFromToRangeFilter(
        field_name='deadline',
        lookup_expr='exact',
        label='deadline'
    ) 
    filterStatus = filters.BooleanFilter(
        field_name = 'status',
        method = 'only_active'
    )
    def only_active(self, querset, status, value):
        valor = 'DONE' if value else 'BACKLOG'
        return querset.filter(status=valor)
class Meta:
    model: RequestTask
    fields = ['filterName']
    
class TaskConFiltro(generics.ListAPIView):
    queryset = RequestTask.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    