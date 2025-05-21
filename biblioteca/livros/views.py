from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import Book, Profile
from .forms import LivroForm, SimpleUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages



def is_admin(user):
    return user.is_authenticated and user.is_staff



def home(request):
    books = Book.objects.all()

    user_books = []
    if request.user.is_authenticated:
        profile, _ = Profile.objects.get_or_create(user=request.user)
        user_books = profile.books.all()

    return render(request, 'home.html', {
        'books': books,
        'user_books': user_books,
    })

def user_login(request):
    users = [
        {'tipo': 'Administrador', 'usuario': 'admin', 'senha': 'admin12345'},
        {'tipo': 'Padrão', 'usuario': 'user', 'senha': 'user'},
    ]

    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'users': users})



def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, 'perfil.html', {'books': profile.books.all()})



@login_required
def add_to_profile(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    profile, _ = Profile.objects.get_or_create(user=request.user)
    profile.books.add(book)
    return redirect('perfil')

@login_required
def remove_from_profile(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    request.user.profile.books.remove(book)
    return redirect('perfil')

@user_passes_test(is_admin)
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('home')
    else:
        form = LivroForm()
    return render(request, 'cadastrar.html', {'form': form})

@user_passes_test(is_admin)
def editar_livro(request, livro_id):
    livro = get_object_or_404(Book, id=livro_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'editar.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def remover_livro(request, livro_id):
    livro = get_object_or_404(Book, id=livro_id)
    livro.delete()
    return redirect('home')

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe.')
                # Aqui, retorna o form com dados para mostrar erro, não vazio
                return render(request, 'register.html', {'form': form})

            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

        else:
            messages.error(request, 'Dados inválidos. Tente novamente.')
            # Retorna o form com os erros para o usuário corrigir
            return render(request, 'register.html', {'form': form})

    else:
        # GET - formulário vazio
        form = SimpleUserCreationForm()
    return render(request, 'register.html', {'form': form})

