from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users/crud', ViewSetUser, basename = 'endpoint de Usuario')
router.register(r'addres/crud', ViewSetAddress, basename = 'endpoint de Domicilio')
router.register(r'login/crud', ViewSetlogin, basename = 'endpoint de login')
urlpatterns = router.urls

