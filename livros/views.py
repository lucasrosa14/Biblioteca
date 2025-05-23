from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from .models import Book, Profile, UserProfile
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
    user = request.user

    try:
        user_profile = user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    # Aqui, busca ou cria sempre um Profile
    profile, _ = Profile.objects.get_or_create(user=user)

    user_books = profile.books.all()
    livros_na_estante = user_books.count()

    context = {
        'user': user,
        'profile': profile,  # perfil de livros
        'user_profile': user_profile,  # perfil pessoal
        'user_books': user_books,
        'livros_na_estante': livros_na_estante,
    }
    return render(request, 'perfil.html', context)



@login_required
def add_to_profile(request, book_id):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    book = get_object_or_404(Book, id=book_id)
    profile.books.add(book)
    return redirect('home')

@login_required
def remove_from_profile(request, book_id):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    try:
        book = Book.objects.get(id=book_id)
        profile.books.remove(book)   # aqui, remove do profile.books, não user.books
        messages.success(request, f'O livro "{book.title}" foi removido da sua estante.')
    except Book.DoesNotExist:
        messages.error(request, 'Livro não encontrado.')
    return redirect('perfil')


@user_passes_test(is_admin)
def cadastrar_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Livro cadastrado com sucesso.")
            return redirect('home')
    else:
        form = LivroForm()
    return render(request, 'cadastrar.html', {'form': form})

@user_passes_test(is_admin)
def editar_livro(request, book_id):
    livro = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'editar.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def remover_livro(request, book_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, "Você não tem permissão para excluir livros.")
        return redirect('home')

    try:
        livro = Book.objects.get(id=book_id)
        livro.delete()
        messages.success(request, "Livro removido com sucesso.")
    except Book.DoesNotExist:
        messages.error(request, "Livro não encontrado ou já removido.")
    
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            sexo = form.cleaned_data.get('sexo')
            data_nascimento = form.cleaned_data.get('data_nascimento')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuário já existe.')
                return render(request, 'register.html', {'form': form})

            # Cria o usuário
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Cria o perfil associado
            UserProfile.objects.create(
                user=user,
                sexo=sexo,
                data_nascimento=data_nascimento
            )

            return render(request, 'register.html', {
                'form': SimpleUserCreationForm(),  # formulário limpo
                'success': True,
                'username': username,
            })
        else:
            messages.error(request, 'Dados inválidos. Tente novamente.')
            return render(request, 'register.html', {'form': form})
    else:
        form = SimpleUserCreationForm()
    return render(request, 'register.html', {'form': form})



