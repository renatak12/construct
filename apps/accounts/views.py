from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.views import View
import requests
from django.http import JsonResponse

from .models import Usuario
from .models import Fornecedor
from .models import Endereco
from .models import Cliente


class Login(View):
    def get(self, request):
        return render(request, 'accounts/registration/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:logado')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
            return redirect('accounts:login')

class SignUp(View):
    def get(self, request):
        return render(request, 'accounts/registration/signup.html')

    def post(self, request):
        nome = request.POST['nome']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        imagem = request.FILES.get('imagem')  

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já está cadastrado.')
            return redirect('accounts:signup')

        try:
            usuario = Usuario.objects.create_user(username=username, email=email, password=password)
            usuario.nome = nome
            usuario.cpf = cpf
            usuario.telefone = telefone
            usuario.imagem = imagem
            usuario.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('accounts:login')
        except ValidationError as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
            return redirect('accounts:signup')


@method_decorator(login_required, name='dispatch')
class Logado(View):
    def get(self, request):
        return render(request, 'accounts/logado.html')
  
    
@method_decorator(login_required, name='dispatch')
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('pages:home')
    
@method_decorator(login_required, name='dispatch')
class Profile(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

    def post(self, request):
        usuario = request.user
        usuario.nome = request.POST.get('nome', usuario.nome)
        usuario.cpf = request.POST.get('cpf', usuario.cpf)
        usuario.telefone = request.POST.get('telefone', usuario.telefone)
        usuario.email = request.POST.get('email', usuario.email)

        # Verifique se o campo 'nova_imagem' existe antes de atribuir a imagem do perfil
        if 'nova_imagem' in request.FILES:
            usuario.imagem = request.FILES['nova_imagem']

        # Verifique se os campos para alterar a senha foram preenchidos
        current_password = request.POST.get('currentPassword')
        new_password = request.POST.get('newPassword')
        renew_password = request.POST.get('renewPassword')

        if current_password and new_password and renew_password:
            # Verifique se a senha atual está correta
            if usuario.check_password(current_password):
                # Verifique se a nova senha e a repetição da senha correspondem
                if new_password == renew_password:
                    # Defina a nova senha usando a função set_password
                    usuario.set_password(new_password)
                    messages.success(request, 'Senha alterada com sucesso!')
                else:
                    messages.error(request, 'A nova senha e a repetição da senha não correspondem. Tente novamente.')
            else:
                messages.error(request, 'A senha atual está incorreta. Tente novamente.')

        try:
            usuario.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao atualizar perfil: {str(e)}')

        return redirect('accounts:profile')


@method_decorator(login_required, name='dispatch')
class UploadImageView(View):
    def post(self, request):
        nova_imagem = request.FILES.get('nova_imagem')
        if nova_imagem:
            request.user.imagem = nova_imagem
            request.user.save()
            messages.success(request, 'Imagem de perfil atualizada com sucesso!')
        return redirect('accounts:profile')
    
@method_decorator(login_required, name='dispatch')
class RemoveImageView(View):
    def get(self, request):
        if request.user.imagem:
            request.user.imagem.delete()
            request.user.save()
            messages.success(request, 'Imagem de perfil removida com sucesso!')
        return redirect('accounts:profile')
    

#================================================================
# VIEWS FORNECEDORES

@method_decorator(login_required, name='dispatch')
class CriarFornecedor(View):
    template_name = 'accounts/fornecedores/criar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        nome = request.POST['nome']
        cnpj = request.POST['cnpj']
        telefone = request.POST['telefone']
        email = request.POST['email']

        # Cria um novo objeto Fornecedor e salvá-lo no banco de dados
        Fornecedor.objects.create(nome=nome, cnpj=cnpj, telefone=telefone, email=email)
        messages.success(request, 'Fornecedor cadastrado com sucesso!')
        
        # Redireciona o usuário para outra página, como a lista de fornecedores
        return redirect('accounts:criar_fornecedor') 

    
@method_decorator(login_required, name='dispatch')
class ListarFornecedor(View):
    template_name = 'accounts/fornecedores/listar.html'

    def get(self, request):
        fornecedores = Fornecedor.objects.all()
        return render(request, self.template_name, {'fornecedores': fornecedores})


@method_decorator(login_required, name='dispatch')
class EditarFornecedor(View):
    template_name = 'accounts/fornecedores/editar.html'

    def get(self, request, fornecedor_id):
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
        return render(request, self.template_name, {'fornecedor': fornecedor})

    def post(self, request, fornecedor_id):
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)

        nome = request.POST['nome']
        cnpj = request.POST['cnpj']
        telefone = request.POST['telefone']
        email = request.POST['email']

        fornecedor.nome = nome
        fornecedor.cnpj = cnpj
        fornecedor.telefone = telefone
        fornecedor.email = email
        fornecedor.save()

        messages.success(request, 'Fornecedor atualizado com sucesso!')

        return redirect('accounts:listar_fornecedor')
    
@method_decorator(login_required, name='dispatch')
class ExcluirFornecedor(View):
    template_name = 'accounts/fornecedores/excluir.html'
    
    def get(self, request, fornecedor_id):
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
        return render(request, self.template_name, {'fornecedor': fornecedor})
    
    def post(self, request, fornecedor_id):
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
        fornecedor.delete()
        messages.success(request, 'Fornecedor excluído com sucesso!')
        
        return redirect('accounts:listar_fornecedor')  

#================================================================
# VIEWS CLIENTES

@method_decorator(login_required, name='dispatch')
class CriarCliente(View):
    template_name = 'accounts/clientes/criar.html' 

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')

        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        cep = request.POST.get('cep')
        cidade_estado_api_url = f'https://viacep.com.br/ws/{cep}/json/'
        cidade_estado_api_response = requests.get(cidade_estado_api_url)
        if cidade_estado_api_response.status_code == 200:
            cidade_estado_data = cidade_estado_api_response.json()
            cidade = cidade_estado_data.get('localidade')
            estado = cidade_estado_data.get('uf')
        else:
            cidade = None
            estado = None

        # Criar o objeto Endereco
        endereco = Endereco.objects.create(
            logradouro=logradouro,
            numero=numero,
            cep=cep,
            cidade=cidade,
            estado=estado
        )

        # Criar o objeto Cliente associado ao endereço criado acima
        Cliente.objects.create(
            nome=nome,
            telefone=telefone,
            cpf=cpf,
            email=email,
            endereco=endereco
        )

        return redirect('accounts:criar_cliente') 
    
class ListarClientes(View):
    template_name = 'accounts/clientes/listar.html'

    def get(self, request):
        clientes = Cliente.objects.all()
        return render(request, self.template_name, {'clientes': clientes})
    

class EditarCliente(View):
    template_name = 'accounts/clientes/editar.html'

    def get(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        return render(request, self.template_name, {'cliente': cliente})

    def post(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        
        # Atualiza os dados do cliente
        cliente.nome = request.POST.get('nome')
        cliente.telefone = request.POST.get('telefone')
        cliente.cpf = request.POST.get('cpf')
        cliente.email = request.POST.get('email')
        
        # Atualiza os dados do endereço
        cliente.endereco.logradouro = request.POST.get('logradouro')
        cliente.endereco.numero = request.POST.get('numero')
        cliente.endereco.cep = request.POST.get('cep')
        cliente.endereco.cidade = request.POST.get('cidade')
        cliente.endereco.estado = request.POST.get('estado')
        
        cliente.endereco.save()  # Salva as mudanças no endereço
        cliente.save()  # Salva as mudanças no cliente
        
        return redirect('accounts:listar_clientes')
    
    
class ExcluirCliente(View):
    template_name = 'accounts/clientes/excluir.html'

    def get(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        return render(request, self.template_name, {'cliente': cliente})

    def post(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        cliente.delete()
        return redirect('accounts:listar_clientes')
