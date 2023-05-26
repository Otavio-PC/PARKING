from django.urls import path
from app.views import CarroViewSet, UsuarioViewSet, GaragemViewSet, MeViewSet, MeGaragensViewSet

urlpatterns = [
    # Carro URLs
    path('carros/', CarroViewSet.as_view({'get': 'list', 'post': 'create'}), name='carro-list'),
    path('carros/<int:pk>/', CarroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='carro-detail'),

    # User URLs
    path('users/', UsuarioViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UsuarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),

    # Garagem URLs
    path('garagens/', GaragemViewSet.as_view({'get': 'list', 'post': 'create'}), name='garagem-list'),
    path('garagens/<int:pk>/', GaragemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='garagem-detail'),

    # Me URL
    path('me/', MeViewSet.as_view(), name='me'),
    # Me Garagens URL
    path('me-garagens/', MeGaragensViewSet.as_view(), name='me-garagens'),

    # #Detalhes do Usuario Logado
    # path('me/', MeView.as_view(), name='me'),

    # path('system-me/', SystemMe.as_view(), name='system-me'),

    # path('system-me-garagens/', SystemMeGaragens.as_view(), name='system-me-garagens')
]
