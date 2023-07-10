from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    
    path('admin/', admin.site.urls),
]
