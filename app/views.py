from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home.html')


# Formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')


# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferenças'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.save()
        user.user_permissions.add(24)
        data['msg'] = 'Usuário cadastrado com sucesso'
        data['class'] = 'alert-sucess'
    return render(request, 'painel.html', data)


# Formulation do panel de login
def painel(request):
    return render(request, 'painel.html')


# Process Login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)


# Pag initial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')


def homeit(request):
    return render(request, 'dashboard/homeit.html')


def homepdf(request):
    return render(request, 'dashboard/homepdf.html')

def logouts(request):
    logout(request)
    return redirect('/painel/')


# alterar a senha corrigir após

def changePassword(request):
    u = User.objects.get(username=request.user.email)
    u.set_password(request.POST['senha'])
    u.save()
    logout(request)
    return redirect('/painel/')

# corrigir essa requisição criar um novo formulário




