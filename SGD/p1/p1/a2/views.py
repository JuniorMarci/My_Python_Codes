#!/usr/bin/env python
#-*- coding: utf-8 -*-

#a2

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Documento

@login_required(login_url='login')
def Tab(request):
	return render(request, "Docs/Tab.html", {'Tab': 'Tab'})

# Create your views here.

from django.shortcuts import render, redirect
from .forms import DocumentoForm

'''
def cadastrar_documento(request):
	if request.method == 'POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Tab')
	else:
		form = DocumentoForm()
	
	context = {'form': form,'todos': Documento.objects.all()}
	return render(request, 'Docs/cadastrar_documento.html', {'form': context['form'],'todos':context['todos']})
'''
	
@login_required(login_url='login')
def cadastrar_documento(request):
	if request.method == 'POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid(): # cria uma instancia do modelo Documento sem salvar no banco de dados
			documento = form.save(commit=False) # altera o atributo arquivo com os valores dos campos nome e sequencia
			documento.arquivo = (
			form.cleaned_data['tipo'] + "_" +
			form.cleaned_data['departamento'] + "_" +
			str(form.cleaned_data['sequencia'])+"_"+
			str(form.cleaned_data['revisao'])			# salva a instancia no banco de dados
			)
			documento.save()
			form = DocumentoForm()
			return redirect('cadastrar_documento', permanent=True)
		
	else: form = DocumentoForm()

	context = {'form': form,'todos': Documento.objects.all()}
	return render(request, 'Docs/cadastrar_documento.html', {'form': context['form'],'todos':context['todos']})

	
@login_required(login_url='login')
def apagar_documento(request, doc):
	arquivo = Documento.objects.filter(arquivo=doc).first()
	#arquivo = Documento.objects.get(arquivo=doc)
	arquivo.delete()
	todos = {'todos': Documento.objects.all(),'mensagem':"Apagado com sucesso!"}
	return render(request,'Docs/cadastrar_documento.html',todos)
	

from django.http import HttpResponseRedirect
from django.conf import settings
import os

def enviar_arquivo(request, doc,rev):
	if request.method == 'POST':
		uploaded_file = request.FILES['arquivo']
		nome_arquivo_original = uploaded_file.name
		extensao_arquivo = os.path.splitext(nome_arquivo_original)[-1]
		#file_path = os.path.join(settings.MEDIA_ROOT, doc+"_"+rev+extensao_arquivo)
		
		# Atualize o campo de revisão
		arquivo = Documento.objects.filter(arquivo=doc).first()
		arquivo.revisao = int(rev)+1
		arquivo.status = 'Aguardando Aprovacao'
		'''
		doc = doc.split('.')[0]
		corte = doc.split('_')
		corte = str(corte[len(corte)-1])
		corte = len(doc)-len(corte)
		doc = doc[0:corte]
		doc = doc#[len(doc)]
		arquivo.arquivo = doc+"_"+(str(int(rev)+1))+'_'+extensao_arquivo #doc[:(len(doc.split('.')[1]))]+"_"+rev+extensao_arquivo
		'''
		arquivo.arquivo = arquivo.arquivo[:len(arquivo.arquivo)-len(arquivo.arquivo.split('_')[-1])]+str(arquivo.revisao)
		arquivo.extensao = extensao_arquivo
		
		file_path = os.path.join(settings.MEDIA_ROOT, arquivo.arquivo+arquivo.extensao)
		
		#arquivo.save()
		
		with open(file_path, 'wb') as destination:
			for chunk in uploaded_file.chunks():
				destination.write(chunk)
				
		arquivo.save()
		
		return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	else:
		# Lógica para lidar com solicitações GET, se necessário
		pass

		
@login_required(login_url='login')
def alterar_status(request):
	if request.method == 'POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid(): # cria uma instancia do modelo Documento sem salvar no banco de dados
			documento = form.save(commit=False) # altera o atributo arquivo com os valores dos campos nome e sequencia
			documento.arquivo = (
			form.cleaned_data['tipo'] + "_" +
			form.cleaned_data['departamento'] + "_" +
			str(form.cleaned_data['sequencia'])+"_"+
			str(form.cleaned_data['revisao'])			# salva a instancia no banco de dados
			)
			documento.save()
			form = DocumentoForm()
			return redirect('cadastrar_documento', permanent=True)
			
	else: form = DocumentoForm()
	
	context = {'form': form,'todos': Documento.objects.all()}
	return render(request, 'Docs/alterar_status.html', {'form': context['form'],'todos':context['todos']})
	
@login_required(login_url='login')
def atualizar_status(request,doc,status):

	print("FOI")
	return redirect('/')
	
@login_required(login_url='login')
def at_st(request,doc,status):
	print("FOI")
	arquivo = Documento.objects.filter(arquivo=doc).first()
	#arquivo.obs = obs
	arquivo.status = status
	arquivo.save()
	#form = AlteraForm()
	#context = {'form': form,'todos': Documento.objects.all()}
	#return render(request, 'Docs/alterar_status.html', {'form': context['form'],'todos':context['todos']})
	# Substitua 'Docs/alterar_status.html' pelo nome do seu modelo HTML, se necessário.
	#return render(request, 'Docs/alterar_status.html', {'form': form, 'todos': context['todos']})
	#return redirect('alterar_status')
	return redirect('/alterar-status/')

def add_obs(request,doc):
	obs = request.GET.get('obs', '') 
	arquivo = Documento.objects.filter(arquivo=doc).first()
	arquivo.obs = obs
	arquivo.save()
	return redirect('/alterar-status/')
	
def rem_obs(request,doc):
	arquivo = Documento.objects.filter(arquivo=doc).first()
	arquivo.obs = ''
	arquivo.save()
	return redirect('/alterar-status/') 