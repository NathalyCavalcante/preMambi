from django.db import models
from django.contrib.auth.models import User  # importa o admin registrado pra usar adiante
# Create your models here.


class Professions(models.Model):
    name = models.CharField(max_length=225) 

    class Meta:
        ordering = ('name',) # pedir a ordem que mostra as categorias - LEMBRAR DA VÍRGULA
        verbose_name_plural = 'Professions' # Django tem problemas com plural, vc tem que avisar a ele.
        
    def __str__(self): # Para avisar ao admim a chamar os itens pelos nomes certos na página.
        return self.name 

class Member(models.Model):
    name = models.CharField(max_length=225)
    phone = models.IntegerField() 
    email = models.EmailField(max_length=100)  
    company = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='members_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)    
    member_since = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True) # coloquei apenas para criar um filtro booleano na hora de criar a view do browser
    created_by = models.ForeignKey(User, related_name="members", on_delete=models.CASCADE) # se deleta um usuário deleta as demais informações
    profession = models.ForeignKey(Professions, related_name="members", on_delete=models.CASCADE) # se deleta uma categoria, deleta todos os membros

    class Meta:
        ordering = ('profession',)
                
    def __str__(self): # Para avisar ao admim a chamar os itens pelos nomes certos na página.
        # código antigo que passou a gerar erro no admin:
        # return self.profession, self.name
        # código novo que, segundo um tutorial, o python 3 fica confuso da maneira antiga.
        template = '{0.profession} - {0.name}'
        return template.format(self)


