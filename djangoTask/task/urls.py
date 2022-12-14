from django.urls import include, path
from rest_framework import routers
from task.views.views import ProjectViewSet, ProjectViewComment

from task.views.views_method_api import method_get_task, method_GPD_task
from task.views.views_method_api import TaskListApiView, TaskEditApiView, TaskListGenericApiView, TaskEditGenericApiView, TaskListConcretaGenericApiView, TaskViewSet, ProjectViewSet, ProjectViewSetLook, TaskConFiltro
from rest_framework.routers import DefaultRouter
# urls de View donde funciona 
# router = routers.DefaultRouter()
# router.register('api/task', ProjectViewSet, 'projects')
# router.register('api/comment', ProjectViewComment, 'comment')
# urlpatterns = router.urls



# URLS de filter
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api/task/', ProjectViewSet.as_view(), name='patients'),
# ]


# URLs de los metodos get post 
router = DefaultRouter()
router.register(r'ViewConjuntTaskSets', ProjectViewSet, basename='ViewConjuntTaskSets')

router.register(r'ViewConjuntTask', TaskViewSet, basename='ViewConjuntTask')
router.register(r'ProjectViewSetLook', ProjectViewSetLook, basename='ProjectViewSetLook')

urlpatterns = [
    path('api/task/', method_get_task, name='GET'),
    path('api/task/<int:pk>', method_GPD_task, name='POST'),
    path('class/task', TaskListApiView.as_view(), name='classTaskList'),
    path('class/task/<int:pk>', TaskEditApiView.as_view(), name='classTasList'),
    path('classGeneric/task/', TaskListGenericApiView.as_view(), name='classGenericTasList'),
    path('classGeneric/task/<int:pk>', TaskEditGenericApiView.as_view(), name='classGenericTaskEdit'),
    path('classConcrete/task/', TaskListConcretaGenericApiView.as_view(), name='classConcreteTaskEdit'),
    path('filtroAgrupados/task/', TaskConFiltro.as_view(), name='TaskConFiltro'),
    path('vistas/', include(router.urls)),
]


