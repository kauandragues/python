
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('escola.urls')),
    path('', RedirectView.as_view(pattern_name='listar_salas', permanent=False)),
    path('accounts/', include('django.contrib.auth.urls')),
]
