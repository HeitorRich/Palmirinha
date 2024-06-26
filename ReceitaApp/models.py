from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome
    
class Receita(models.Model):
    dificuldade = [
        ("Easy", "Fácil"),
        ("Moderate", "Moderado"),
        ("Hard", "Difícil")
    ]
    nome = models.CharField(max_length = 50)
    ingredientes = models.TextField(max_length = 2000)
    modo_de_preparo = models.TextField(max_length = 8000)
    grau_de_dificuldade = models.CharField(max_length=8, choices=dificuldade)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tempo_de_preparo =  models.TimeField(max_length = 3, null = True, blank = True, help_text="Minutos")
    creditos = models.CharField(max_length = 50, null = True, blank = True)
    fonte = models.CharField(max_length = 100, null = True, blank = True)


    def __str__(self):
        return self.nome