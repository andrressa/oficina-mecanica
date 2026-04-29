from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, VeiculoViewSet, OrdemServicoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'ordens', OrdemServicoViewSet)

urlpatterns = router.urls
