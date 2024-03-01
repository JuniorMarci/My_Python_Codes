"""
URL configuration for p1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


from a1 import views
import a1.MySystem.SystemViews as VS
from a2 import views as aa

from django.views.static import serve

# marcio.souza@partage.com.br
#123

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.v1,name="v1"),
	path('',aa.cadastrar_documento,name="v1"),
    path('sv1/',VS.sv1,name="sv1"),
    path('lista/',views.v2,name="v2"),
    path('lista/apagar/',views.v3,name="v3"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('cadastrar/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('NovoCadastrar/', views.NovoCadastro, name="NovoCadastro"),
    path('apagar/<str:email>/', views.apagar_usuario, name='apagar_usuario'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    path('trocarSenha/', views.change_password, name='change_password'),
    path('SenhaAlterada/', views.SenhaAlterada, name='SenhaAlterada'),
	
	path('Tab/', aa.Tab, name='Tab'),
	path('cadastrar-documento/', aa.cadastrar_documento, name='cadastrar_documento'),
	path('apagar-documento/<str:doc>/', aa.apagar_documento, name='apagar_documento'),
	path('enviar-arquivo/<str:doc>/<str:rev>', aa.enviar_arquivo, name='enviar_arquivo'),
	path('alterar-status/', aa.alterar_status, name='alterar_status'),
	path('atualizar-status/<str:doc>/<str:status>',aa.atualizar_status, name='atualizar_status'),
	path('at-st/<str:doc>/<str:status>',aa.at_st, name='at_st'),
	path('add-obs/<str:doc>/',aa.add_obs, name='add_obs'),
	
	#path('todas_metas/',aa.todas_metas, name='todas_metas'),
	#path('add-obs/<str:doc>/<str:obs>',aa.add_obs, name='add_obs'),
	
	
]


# urls.py

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
