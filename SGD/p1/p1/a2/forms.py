from django import forms
from .models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['nome', 'tipo', 'departamento', 'sequencia','revisao','versao','status']
		#widgets = {'nome': forms.TextInput(attrs={'class': 'nome', 'style': 'width: 300px;'})}
		
class AlteraForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['nome','status','obs']
		#widgets = {'nome': forms.TextInput(attrs={'class': 'nome', 'style': 'width: 300px;'})}