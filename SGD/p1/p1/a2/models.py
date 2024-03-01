from django.db import models

class Documento(models.Model):
	nome = models.CharField(max_length=100)
	tipo = models.CharField(max_length=100)
	departamento = models.CharField(max_length=100)
	sequencia = models.IntegerField()
	arquivo = models.CharField(max_length=255,blank=True)
	extensao = models.CharField(max_length=5,blank=True)
	revisao = models.IntegerField()
	versao = models.CharField(max_length=100)
	Status = STATUS_CHOICES = [
	('Aprovado', 'Aprovado'),
	('Reprovado', 'Reprovado'),
	('Necessita Alteracao', 'Necessita Alteracao'), ]
	status = models.CharField(max_length=100, choices=Status)
	obs = models.CharField(max_length=500,blank=True)
	
	