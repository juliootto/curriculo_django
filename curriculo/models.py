from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Escolaridade(models.Model):
    instituicao_ensino = models.CharField(max_length=100,null=False,blank=False)
    curso = models.CharField(max_length=100,null=False,blank=False)
    inicio = models.DateField(blank=False)
    fim = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.instituicao_ensino
    
class ExperienciaProficional(models.Model):
    empresa = models.CharField(max_length=100,null=False,blank=False)
    cargo = models.CharField(max_length=100,null=False,blank=False)
    descricao = models.TextField(null=False, blank=False)
    inicio = models.DateField(blank=False)
    fim = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return self.empresa
    
class Cursos(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    empresa = models.CharField(max_length=100,null=False,blank=False)
    certificado = models.FileField(upload_to="certificados/",blank=True)
    inicio = models.DateField(blank=False)
    fim = models.DateField(blank=True,null=True)   
    
    def __str__(self):
        return self.nome
    
class Contato(models.Model):
    nome = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    telefone = PhoneNumberField(region='BR')
    mensagem = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
class Interesses(models.Model):
    interesse = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.interesse
    