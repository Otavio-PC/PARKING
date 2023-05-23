from django.urls import path, include
from app.views import UserViewSet, CarroViewSet, GaragemViewSet
from rest_framework.routers import DefaultRouter

app_name = 'app'

# Create the router instance
router = DefaultRouter(trailing_slash=False)

# Register the view sets with the router
router.register('user', UserViewSet, basename='user')
router.register('carro', CarroViewSet, basename='carro')
router.register('garagem', GaragemViewSet, basename='garagem')

urlpatterns = [
    path('', include(router.urls)),
    # Other API-specific URLs for your app
]
