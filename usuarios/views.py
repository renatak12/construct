from curses.ascii import HT
import imp
from django.http import HttpResponse
from django.shortcuts import render
from rolepermissions.decorators import has_permission_decorator
from .models import Users
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

#@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
    if request.method == "GET":
        vendedores = Users.objects.filter(cargo="V")
        return render(request, 'cadastrar_vendedor.html', {'vendedores': vendedores})
    if request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = Users.objects.filter(email=email)

        if user.exists():
            # TO DO: Utilizar messages do django
            #return HttpResponse('Email já existe')
            messages.add_message(request, messages.INFO, 'Email já Existe')
        
        user = Users.objects.create_user(username=email,
                                            email=email,
                                            password=senha,
                                            first_name=nome,
                                            last_name=sobrenome,
                                            cargo="V")

        # Redirecionar com uma mensagem
        #return HttpResponse('Conta criada')
        messages.add_message(request, messages.SUCCESS, 'Cadastrado realizado com sucesso')
        return redirect(reverse('cadastrar_vendedor'))

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            #return redirect(reverse('index'))
            return render(request, 'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            # TO DO: Redirecionar com mensagem de erro
            messages.add_message(request, messages.ERROR, 'Usuário invalido')
            #return HttpResponse('Usuário invalido')
        
        auth.login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Usuário logado com sucesso')
        return redirect(reverse('index'))
        #return HttpResponse('Usuário logado com sucesso')
        #return render(request, 'login.html')
    
def logout(request):
    request.session.flush()
    messages.add_message(request, messages.SUCCESS, 'Usuário deslogado com sucesso')
    return redirect(reverse('login'))

#@has_permission_decorator('cadastrar_vendedor')
def excluir_usuario(request, id):
    vendedor = get_object_or_404(Users, id=id)
    vendedor.delete()
    messages.add_message(request, messages.SUCCESS, 'Vendedor excluido com sucesso')
    return redirect(reverse('cadastrar_vendedor'))
