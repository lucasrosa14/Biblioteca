# Imagem base com Python
FROM python:3.12-slim

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . /app/

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta padrão do Django
EXPOSE 8000

# Comando para rodar o servidor
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

