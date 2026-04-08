from django.db import models

class Slide(models.Model):
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='carrossel/')
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['ordem']
