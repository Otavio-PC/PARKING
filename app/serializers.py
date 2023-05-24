from rest_framework import serializers
from app.models import CarroModel, GaragemModel, UserModel
from django.contrib.auth.models import User


class CarroSerializer(serializers.ModelSerializer):
    # CarroSerializer implementation

    class Meta:
        model = CarroModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    colecao = CarroSerializer(many=True, required=False)
    
    class Meta:
        model = UserModel
        fields = '__all__'

class GaragemSerializer(serializers.ModelSerializer):
    estacionados = CarroSerializer(many=True, required=False)

    class Meta:
        model = GaragemModel
        fields = '__all__'
