#a1

from django.contrib.auth.decorators import login_required


from django.shortcuts import render
from .models import Tab

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def v1(request):
    if request.user.is_authenticated: STATUS = "Sair"
    else: STATUS = "Fazer Login"
    return render(request, "h1.html", {'STATUS': STATUS})


def v2(request):

    #return render(request,"h2.html")
    if request.method == "POST":
        entrada = Tab()
        Nome = request.POST.get('Nome')
        email = request.POST.get('e-Mail')
        entrada.nome = Nome
        entrada.email = email
        entrada.save()

    todos = {'todos': Tab.objects.all()}

    return render(request,'h2.html',todos)


    #usuarios = CustomUser.objects.all()
    #return render(request, 'lista_usuarios.html', {'usuarios': usuarios})



from django.shortcuts import render, redirect
from .models import Tab

def v3(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        entrada = Tab.objects.get(id=id)
        entrada.delete()
        return redirect('v2')
    else:
        return redirect('v2')




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import LoginForm

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                erro = ""
                return redirect('v1')  # substitua 'home' pelo nome da sua página inicial
            else:
                #form.add_error(None, 'Credenciais inválidas.')
                erro = 'Credenciais inválidas'
        return render(request, 'login.html', {'form': form, 'erro':erro})




from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CadastroForm
from .models import CustomUser
from .models import CustomUserManager

@login_required(login_url='login')
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            nome_usuario = form.cleaned_data['nome']
            messages.success(request, f"Usuário '{nome_usuario}' cadastrado com sucesso!")
            return redirect('cadastrar_usuario')  # Redirecionar para a página de cadastro
    else:
        form = CadastroForm()

    context = {
        'form': form,
        'todos': CustomUser.objects.all(),
    }
    return render(request, 'cadastro.html', context)


@login_required(login_url='login')
def apagar_usuario(request, email):
    usuario = CustomUser.objects.get(email=email)
    usuario.delete()
    todos = {'todos': CustomUser.objects.all(),'mensagem':"Apagado com sucesso!"}
    return render(request,'cadastro.html',todos)

from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

@login_required(login_url='login')
def NovoCadastro(request):
    if request.method == "POST":
        entrada = CustomUser()
        Nome = request.POST.get('Nome')
        email = request.POST.get('e-Mail')
        password = request.POST.get('senha')  # Obtenha a senha do formulário

        try:
            entrada.nome = Nome
            entrada.email = email
            entrada.password = make_password(password)  # Defina a senha usando make_password()
            entrada.save()
            todos = {'todos': CustomUser.objects.all(),'mensagem':"Cadastrado com sucesso!"}
            return render(request,'cadastro.html',todos)

        except IntegrityError:
            todos = {'todos': CustomUser.objects.all(),'mensagem':"Usuario ja cadastrado"}
            return render(request,'cadastro.html',todos)

    todos = {'todos': CustomUser.objects.all(),'mensagem':""}
    return render(request,'cadastro.html',todos)



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm

@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user = request.user
                user.set_password(password)
                user.save()
                messages.success(request, 'Senha alterada com sucesso!')
                return redirect('SenhaAlterada')
            else:
                messages.error(request, 'As senhas não coincidem.')
    else:
        form = ChangePasswordForm()

    context = {'form': form}
    return render(request, 'change_password.html', context)


def SenhaAlterada(request):
    return render(request, 'senhaAlterada.html')