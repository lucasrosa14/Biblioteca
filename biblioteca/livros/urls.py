from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('add/<int:book_id>/', views.add_to_profile, name='add_to_profile'),
    path('remove/<int:book_id>/', views.remove_from_profile, name='remove_from_profile'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('editar/<int:livro_id>/', views.editar_livro, name='editar_livro'),
    path('remover/<int:livro_id>/', views.remover_livro, name='remover_livro'),
    


]
