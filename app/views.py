from rest_framework import viewsets
from app.models import CarroModel, GaragemModel, UsuarioModel
from app.serializers import CarroSerializer, GaragemSerializer, UsuarioSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import UsuarioSerializer, CarroSerializer, GaragemSerializer
from .models import UsuarioModel, CarroModel, GaragemModel

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer

class CarroViewSet(viewsets.ModelViewSet):
    queryset = CarroModel.objects.all()
    serializer_class = CarroSerializer

class GaragemViewSet(viewsets.ModelViewSet):
    queryset = GaragemModel.objects.all()
    serializer_class = GaragemSerializer

class MeViewSet(APIView): # retorna informaçoes do usuario logado, assim como seus carros (frota) e garagens em uso
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        usuario = UsuarioModel.objects.get(user_id=user.id)
        serializer = UsuarioSerializer(usuario)

        return Response(serializer.data)

class MeGaragensViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        usuario = UsuarioModel.objects.get(user_id=user.id)
        carros = CarroModel.objects.filter(dono=usuario)
        garagens = []

        for carro in carros:
            if carro.estacionado_em:
                garagens.append(carro.estacionado_em)

        if garagens:
            serializer = GaragemSerializer(garagens, many=True)
            return Response(serializer.data)

        return Response([])

# class Garagens(APIView): # retorna as garagens em uso e as informaçoes das mesmas.
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         usuario = UserModel.objects.get(user_id=request.user.id)
    

        

# sobre a forma de lidar com uma view:
# caso impletametada como viewset, os metodos do CRUD e HTTP serao definidos na urls.py
# caso implementada como APIView, os metodos de CRUD e HTTP serao definidos na propria views.py

# class UsuarioViewSet(viewsets.ModelViewSet):
#     queryset = UsuarioModel.objects.all()
#     serializer_class = UsuarioSerializer

# class CarroViewSet(viewsets.ModelViewSet):
#     queryset = CarroModel.objects.all()
#     serializer_class = CarroSerializer

# class GaragemViewSet(viewsets.ModelViewSet):
#     queryset = GaragemModel.objects.all()
#     serializer_class = GaragemSerializer

# class Me(APIView): # retorna informaçoes do usuario logado, assim como seus carros (frota) e garagens em uso
#     pass

# class Garagens(APIView): # retorna as garagens em uso e as informaçoes das mesmas.
#     pass

# # sobre a forma de lidar com uma view:
# # caso impletametada como viewset, os metodos do CRUD e HTTP serao definidos na urls.py
# # caso implementada como APIView, os metodos de CRUD e HTTP serao definidos na propria views.py

# # class CarroViewSet(viewsets.ModelViewSet):
# #     queryset = CarroModel.objects.all()
# #     serializer_class = CarroSerializer

# # class UserViewSet(viewsets.ModelViewSet):
# #     queryset = UserModel.objects.all()
# #     serializer_class = UserModelSerializer

# # class GaragemViewSet(viewsets.ModelViewSet):
# #     queryset = GaragemModel.objects.all()
# #     serializer_class = GaragemSerializer

# # class MeView(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         user = request.user
# #         serializer = UserSerializer(user)
# #         return Response(serializer.data)

# # class SystemMe(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         try:
# #             user = UserModel.objects.get(user_id=request.user.id)
# #             print(user)
# #             print(user.id)
# #             print(isinstance(user, UserModel))
# #             serializer = UserModelSerializer(user)
# #             return Response(serializer.data)
# #         except UserModel.DoesNotExist:
# #             raise status.HTTP_404_NOT_FOUND

# # class SystemMeGaragens(APIView):
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         try:
# #             user = UserModel.objects.get(user_id=request.user.id)
# #             carros = CarroModel.objects.filter(dono_id=user.id)
            
# #             garagens = []
# #             for carro in carros:
# #                 garagem = GaragemModel.objects.filter(id=carro.garagem_id).first()
# #                 if garagem:
# #                     garagens.append(garagem)

# #             serializer = GaragemSerializer(garagens, many=True)
# #             return Response(serializer.data)
# #         except UserModel.DoesNotExist:
# #             raise status.HTTP_404_NOT_FOUND

#  #   def get(self, request):
#   #      try:
#    #         user = UserModel.objects.get(user_id=request.user.id)
#     #        carros = CarroModel.objects.filter(dono_id=user.id)
#      #       print(list(carros))
#       #      garagens = []
#        #     for carro in carros:
#        #         garagem = GaragemModel.objects.filter(id=carro.garagem_id)
#        #         if garagem != 0:
#        #             garagens.append(garagem)
#         #    serializer = GaragemSerializer(garagens, many=True)
#       #      if garagens != []|
# #
#  #               for garagem in garagens:
# #
#  #                   serializer = GaragemSerializer(garagem)
#   #                  serializers.append(serializers.data)

        
            
#        #     print(garagens)
#  #           print(list(carros))
#   #          for carro in carros:
#      #           print(carro)
# #            garagens = GaragemModel.objects.filter(id=garagem_id))
#  #           print(carros)
#   #          print(isinstance(carros, list))
#    #         print(isinstance(carros, dict))
#     #        print(carros)
#    #         print(carros.id)
#  #           print(isinstance(carros, CarroModel))
#   #          garagem = GaragemModel.objects.get()

#   #          return Response(serializer.data)
#    #     except UserModel.DoesNotExist:
# ##            raise status.HTTP_404_NOT_FOUND
