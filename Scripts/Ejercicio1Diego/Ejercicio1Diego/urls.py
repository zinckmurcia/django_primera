from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_aplicacion.urls')),  # Esto incluye las URLs definidas en mi_aplicacion
]
