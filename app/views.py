from rest_framework import viewsets, permissions
from app.models import UserModel, CarroModel, GaragemModel
from app.serializers import UserSerializer, CarroSerializer, GaragemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarroViewSet(viewsets.ModelViewSet):
    queryset = CarroModel.objects.all()
    serializer_class = CarroSerializer
    permission_classes = [permissions.IsAuthenticated]

class GaragemViewSet(viewsets.ModelViewSet):
    queryset = GaragemModel.objects.all()
    serializer_class = GaragemSerializer
    permission_classes = [permissions.IsAuthenticated]