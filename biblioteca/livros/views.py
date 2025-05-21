from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, Profile
from .forms import LivroForm

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect

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
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

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
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render(request, 'editar_livro.html', {'form': form})

@user_passes_test(is_admin)
def remover_livro(request, livro_id):
    livro = get_object_or_404(Book, id=livro_id)
    livro.delete()
    return redirect('home')