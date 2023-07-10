from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home' ),
    path('about/', views.About.as_view(), name='about' ),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logado/', views.Logado.as_view(), name='logado'),
    
]
