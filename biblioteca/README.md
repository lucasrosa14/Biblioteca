# 📚 Biblioteca - Sistema de Gerenciamento de Livros

Este é um sistema web de gerenciamento de uma biblioteca, desenvolvido com **Django**. Ele permite que usuários cadastrem-se, façam login, visualizem uma lista de livros, adicionem livros ao seu perfil pessoal (sua "estante") e, no caso de administradores, que cadastrem, editem e removam livros do acervo.

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Django** - Framework web principal.
- **SQLite** - Banco de dados padrão para desenvolvimento.
- **HTML + CSS** - Templates com `Django Template Language`.
- **Bootstrap** - Estilização básica.
- **Mensagens do Django** - Para feedbacks ao usuário.
- **Sistema de autenticação** - Nativo do Django.
- **Uploads de imagem** - Para capas de livros.

## 🖼️ Funcionalidades principais

- ✅ Cadastro e autenticação de usuários.
- ✅ Perfis de usuários com informações pessoais.
- ✅ Estante personalizada para cada usuário.
- ✅ CRUD completo de livros (apenas para administradores).
- ✅ Upload de capas de livros ou uso de links externos.
- ✅ Mensagens de feedback ao adicionar ou remover livros.
- ✅ Modal de confirmação para remoção de livros da estante.

## 🧩 Estrutura do projeto

- `models.py`: Modelos de dados para Livro (`Book`), Perfil (`Profile`) e `UserProfile`.
- `views.py`: Lógica para autenticação, cadastro de livros e perfil de usuário.
- `templates/`: Páginas HTML do sistema.
- `static/`: Arquivos de estilo CSS.
- `urls.py`: Rotas principais.
- `forms.py`: Formulários personalizados.
- `media/`: Onde as capas de livros são armazenadas (quando enviadas).

---

## ⚙️ Como instalar e rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/lucasrosa14/biblioteca.git
cd biblioteca
```
### 2. Crie e ative um ambiente virtual
```
python -m venv venv
# Ativar no Windows:
venv\Scripts\activate
# Ou no macOS/Linux:
source venv/bin/activate
```
### 3. Instale as dependências
```
pip install -r requirements.txt
```
### 4. Aplique as migrações
```
python manage.py migrate
```
### 5. Execute o servidor de desenvolvimento
```
python manage.py runserver
```
Acesse o sistema em:
👉 http://127.0.0.1:8000/


### 📝 Contexto da aplicação
Este sistema foi desenvolvido como um projeto de estudo para praticar:

CRUD com Django.

Sistema de autenticação e perfis de usuário.

Relacionamentos entre modelos (ManyToMany, OneToOne).

Upload e exibição de arquivos de mídia.

Mensagens de feedback com django.contrib.messages.

Implementação de permissões: diferenciação entre usuário padrão e administrador.

###  ✨ Como contribuir
Faça um fork deste repositório.

Crie uma branch: git checkout -b feature/nova-funcionalidade.

Commit suas alterações: git commit -m 'Adiciona nova funcionalidade'.

Push: git push origin feature/nova-funcionalidade.

Abra um Pull Request.

### 📄 Licença
Este projeto está sob a licença MIT.
Veja o arquivo LICENSE para mais detalhes.

### 👨‍💻 Autor
[Lucas Souza da Rosa](https://www.linkedin.com/in/lucas-souza-da-rosa/)