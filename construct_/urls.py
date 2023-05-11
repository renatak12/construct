from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.global_settings import STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)