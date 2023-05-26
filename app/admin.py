from django.contrib import admin
from .models import UsuarioModel, CarroModel, GaragemModel
# Register your models here.

admin.site.register(UsuarioModel)
admin.site.register(CarroModel)
admin.site.register(GaragemModel)
