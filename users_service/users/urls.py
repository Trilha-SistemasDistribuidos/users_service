from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from . import views


router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('registrar/', UsuarioViewSet.as_view({'post': 'create'}), name='registrar_usuario'),
    path('', include(router.urls)),
    path('usuario/<int:pk>/', views.UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail-view'),
    path('usuario/', views.UsuarioCreateListView.as_view(), name='usuario-create-list'),
]