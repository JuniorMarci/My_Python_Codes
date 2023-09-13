import pandas as pd
import os
#import seaborn
import matplotlib.pyplot as plt

def teste():
    return 'Foi'

def converterPNUM(Tab,Col):
    Tab[Col] = Tab[Col].str.replace(",", ".").astype(float)


def Agrupar(Tab,Coluna,Metrica): return Tab[[Coluna,'Previsto Pontual','Realizado Pontual','Nota Pontual','Nota Acumulado','Realizado Acumulado','Previsto Acumulado']].groupby([Coluna]).mean().sort_values(Metrica,ascending=False)

def Abreviar(num):
    if(num==-1):
        return ""
    else:
        tam = len(str(int(num)))
        if(tam>3): numc = str(int(num/1000))+'m'
        if(tam>6): numc = str(int(num/1000000))+'M'
        try: return numc
        except: return str(num)

def GerGrafico(df,ex,ey,ez,Cat,Od):

    df = df.reset_index()
    df[ey] = df[ey].astype(int)

    # Cores de exemplo
    if(ez!=""):
        try: colors = ['w' if value < 0 else 'r' if value < 90 else 'y' if value < 99.9 else 'g' for value in df['Nota Pontual']]
        except: colors = ['w' if value < 0 else 'r' if value < 90 else 'y' if value < 99.9 else 'g' for value in df[ey]]
    else: colors = ['w' if value < 0 else 'r' if value < 90 else 'y' if value < 99.9 else 'g' for value in df[ey]]

    plt.figure(figsize=(20,9))

    if(ez!=""): plt.plot(df[df[ez]>-1].index, df[df[ez]>-1][ez],linestyle='dashed', linewidth=2, markersize=30) #Criar gráfico de linhas

    # Criar o gráfico de barras
    ax = plt.bar(df.index, df[ey], color=colors, width=0.5)

    # Adicionar os valores no topo das barras
    for bar in ax:
        # Obter as coordenadas x e y do texto
        x = bar.get_x() + bar.get_width() / 2
        y = bar.get_height() + 0.1

        # Adicionar o texto com o valor da barra
        #plt.text(x, y, str(bar.get_height()), ha='center', va='bottom', fontsize=25)
        plt.text(x, y, Abreviar(bar.get_height()), ha='center', va='bottom', fontsize=25)

    #plt.axis('off')

    # Ajuste as propriedades dos eixos
    eixos = plt.gca()  # Obtenha os eixos atuais

    # Oculte os contornos dos lados direito e superior
    eixos.spines['top'].set_visible(False)
    eixos.spines['right'].set_visible(False)

    plt.axhline(0, color='gray', linestyle='-') # Adicionando linha no eixo zero

    # Configurar os rótulos do eixo x com os nomes
    plt.xticks(df.index, df[ex],rotation=30,fontsize=25)
    try:
        Minimo = min(df[ey])
        Maximo = max(df[ey])
        if (Maximo<=-1): plt.yticks([0,Minimo,Maximo],fontsize=30)
        elif(Minimo<=-1): plt.yticks([Minimo,0,Maximo],fontsize=30)
        else: plt.yticks([0,Minimo,Maximo],fontsize=30)

    except: print('Sem min/máx')

    # Mostrar o gráfico
    #Nome = '../Graficos/'+str(str(Od)+" - "+ey+" - "+ex+"{ EX -- Cat }"+Cat+'.PNG')
    Nome = '../Graficos/'+str(str(Od)+" - "+ey+' - '+Cat+'.PNG')
    plt.savefig(Nome,dpi=150)
    #plt.show()
    plt.close()



def Filtrar(TabMetas,mes,ona,ColFil,ColIg):
    if(mes != ""): TabMetas = TabMetas[TabMetas['mês']==mes]
    if(ona): TabMetas = TabMetas[TabMetas['Nota Acumulado']>-1] # Desconsidera somente os valores "N/A" Mereo (convertidos como -1)
    if(~ona): TabMetas = TabMetas[~ pd.isna(TabMetas['Nota Pontual'])] # Desconsidera somente os valores "nan" Python, que significam campos vazios
    if(~ona): TabMetas = TabMetas[~ pd.isna(TabMetas['Realizado Pontual'])]
    if(ColFil != ""): TabMetas = TabMetas[TabMetas[ColFil]==ColIg]
    return TabMetas


def Odf(Od):
    Od = int(Od)
    Od = Od+1
    if (int(Od)<100): Od='0'+str(int(Od))
    if (int(Od)<10): Od='00'+str(int(Od))
    return (Od)


def NumPMes(Coluna):
    Meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
    mêsT = Coluna
    for MM in Meses:
        try: mêsT = mêsT.replace(Meses.index(MM)+1,MM)
        except Exception as e: print('Erro T:',e)

    return mêsT





#import plotly.express as px
#import plotly.graph_objects as go

def GerGraficoP(df, ex, ey, ez, Cat, Od):
    df[ey] = df[ey].astype(int)

    # Cores de exemplo
    if ez != "":
        try:
            colors = ['white' if value < 0 else 'red' if value < 90 else 'yellow' if value < 99.9 else 'green' for value in df['Nota Pontual']]
        except:
            colors = ['white' if value < 0 else 'red' if value < 90 else 'yellow' if value < 99.9 else 'green' for value in df[ey]]
    else:
        colors = ['white' if value < 0 else 'red' if value < 90 else 'yellow' if value < 99.9 else 'green' for value in df[ey]]

    # Criar o gráfico de barras
    fig = go.Figure(data=[
        go.Bar(
            x=df.index,
            y=df[ey],
            marker_color=colors,
            width=0.5
        )
    ])

    # Adicionar os valores no topo das barras
    for index, value in enumerate(df[ey]):
        fig.add_annotation(
            text=str(value),
            x=index,
            y=value + 0.1,
            showarrow=False,
            font=dict(size=25)
        )

    # Configurar o layout do gráfico
    fig.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=list(df.index),
            ticktext=list(df[ex]),
            tickangle=30,
            tickfont=dict(size=25),
        ),
        yaxis=dict(
            tickvals=[0, min(df[ey]), max(df[ey])],
            tickfont=dict(size=30),
        ),
        title=dict(text=str(Od) + " - " + ey + ' - ' + Cat),
        showlegend=False,
        xaxis_title=ex,
        yaxis_title=ey
    )

    # Adicionar a linha horizontal no eixo zero
    fig.add_shape(go.layout.Shape(
        type="line",
        x0=-0.5,
        x1=len(df.index) - 0.5,
        y0=0,
        y1=0,
        line=dict(color="gray", dash="solid")
    ))

    # Salvar o gráfico
    Nome = '../Graficos/' + str(Od) + " - " + ey + ' - ' + Cat + '.PNG'
    fig.write_image(Nome, width=1200, height=600, scale=2)

