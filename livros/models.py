from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)
    capa_url = models.URLField(max_length=300, blank=True, null=True)

    users = models.ManyToManyField(User, related_name='books') 
    def get_capa(self):
        # Prioriza o upload, se não tiver, usa a URL
        if self.capa:
            return self.capa.url
        elif self.capa_url:
            return self.capa_url
        return None

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
class UserProfile(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

