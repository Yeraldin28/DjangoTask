from rest_framework import routers
from .api import ProjectViewSet, ProjectViewComment
router = routers.DefaultRouter()

router.register('api/task', ProjectViewSet, 'projects')
router.register('api/comment', ProjectViewComment, 'comment')

urlpatterns = router.urls

