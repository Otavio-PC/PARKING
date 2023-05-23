from rest_framework import serializers
from app.models import CarroModel, GaragemModel, UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['nome', 'email']

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarroModel
        fields = ['nome','modelo', 'cor']

class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GaragemModel
        fields = ['numero']