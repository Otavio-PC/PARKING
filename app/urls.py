from django.urls import path, include
from app.views import Garagens, Me
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("garagens/", Garagens.as_view(), name="Garagens")
]
