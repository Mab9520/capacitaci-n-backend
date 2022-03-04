from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'workers/crud', ViewSetWorker, basename="Endpoint de Trabajador")
router.register(r'workerType/crud', ViewSetWorkerTypeWork, basename="endpoint de tipos")
router.register(r'login/crud', ViewSetLogin, basename="endpoint de login")
urlpatterns = router.urls