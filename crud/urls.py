from rest_framework import routers
from .api import ProjectViewSet


router=routers.DefaultRouter()

router.register('api/crud',ProjectViewSet,'crud')


urlpatterns = router.urls

