from django.contrib import admin
from .models import UserModel, CarroModel, GaragemModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(CarroModel)
admin.site.register(GaragemModel)
