from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Include your app's URLs here
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Other URL patterns for your project
]
