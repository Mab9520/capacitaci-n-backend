from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'type/crud', ViewSetType, basename="endpoint para Tipos pokemon")
router.register(r'Attack/crud', ViewSetAttack, basename="Endpoint para ataques")
router.register(r'Pokemon/crud', ViewSetPokemon, basename="Endpoint de Pokemon")
router.register(r'Entrenador/crud', ViewSetCoachPokemon, basename="Endpoint de entrenador")
router.register(r'login/crud', ViewSetLogin, basename="endpoint de login")
urlpatterns = router.urls