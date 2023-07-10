from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')


class About(View):
    def get(self, request):
        return render(request, 'about.html')


class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:logado')  # redirecione para a página logado após o login
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
            return redirect('core:login')


class SignUp(View):
    def get(self, request):
        return render(request, 'registration/signup.html')

    def post(self, request):
        nome = request.POST['nome']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já está cadastrado.')
            return redirect('core:signup')
        
        try:
            usuario = Usuario.objects.create_user(username=username, email=email, password=password)
            usuario.nome = nome
            usuario.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('core:login')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
            return redirect('core:signup')
        

@method_decorator(login_required, name='dispatch')
class Logado(View):
    def get(self, request):
        return render(request, 'registration/logado.html')
    
    


        
