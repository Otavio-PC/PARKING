from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from app.models import UserModel, CarroModel, GaragemModel
from app.serializers import UserSerializer, CarroSerializer, GaragemSerializer

class Me(APIView):
    pass

class Garagens(APIView):
    def get(self, request):
        print(request.user)
        garagens = GaragemModel.objects.all()
        data = GaragemSerializer(garagens, many=True).data
        return Response(data)