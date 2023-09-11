import pandas as pd
import os
#import seaborn
import matplotlib.pyplot as plt
from Funcoes import converterPNUM, Agrupar, GerGrafico, Filtrar, Odf

#print(os.listdir('..\..\\Correções (V2)\\Saída_Algoritmo'))

TabMetas = r"..\..\Correções (V2)\Saída_Algoritmo\Metas.csv"
TabMetas = pd.read_csv(TabMetas,sep=";", thousands='.')

converterPNUM(TabMetas,'Previsto Pontual')
converterPNUM(TabMetas,'Realizado Pontual')
converterPNUM(TabMetas,'Nota Pontual')
converterPNUM(TabMetas,'Nota Acumulado')
converterPNUM(TabMetas,'Realizado Acumulado')
converterPNUM(TabMetas,'Previsto Acumulado')

Categorias = r"..\..\Correções (V2)\Saída_Algoritmo\Categorias.csv"
Categorias = pd.read_csv(Categorias,sep=";", names=['Cod.Unico','Shopping'],skiprows=1)

TabMetas['Departamento'] = [str(meta).split('_')[0] for meta in TabMetas['Código da Meta']]
TabMetas = TabMetas.merge(Categorias, on='Cod.Unico', how='right')#.to_csv("Right.csv",sep=';')


#colors = ['r' if value < 90 else 'y' if value < 99 else 'g' for value in GRUPO['Nota Acumulado']]

#TabMetas['Nota Acumulado'] = TabMetas['Nota Acumulado'].str.replace(',', '.').astype(float)

def GerarApresentacao(TabFiltrada,Dep, mes):
    TabMetas = TabFiltrada

    Od = Odf(-1)
    Tdf = []

    GRUPODep = Filtrar(TabMetas,mes,True,'','')
    GRUPODep = Agrupar(GRUPODep,'Departamento',"Nota Acumulado")
    GerGrafico(GRUPODep,'Departamento','Nota Acumulado',"",'',Od)
    Od = Odf(Od)
    Tdf.append(GRUPODep)

    for c in GRUPODep.index:
        print(c)
        GRUPOSh = Filtrar(TabMetas,mes,True,'Departamento',c)
        GRUPOShA = Agrupar(GRUPOSh,'Shopping',"Nota Acumulado")
        if (len(GRUPODep.index) > 1): GerGrafico(GRUPOShA,'Shopping','Nota Acumulado',"",c,Od)
        Od = Odf(Od)
        Tdf.append(GRUPOSh)


        for d in GRUPOShA.index:
            print(d)
            GRUPOCol = Filtrar(GRUPOSh,mes,True,'Shopping',d)
            GRUPOColA = Agrupar(GRUPOCol,'Login',"Nota Acumulado")
            GerGrafico(GRUPOColA,'Login','Nota Acumulado',"",c+"-"+d,Od)
            Od = Odf(Od)
            Tdf.append(GRUPOCol)

            for e in GRUPOColA.index:
                print(e)
                GRUPOMet = Filtrar(GRUPOCol,mes,True,'Login',e)
                GRUPOMetA = Agrupar(GRUPOMet,'Código da Meta',"Nota Acumulado")
                GerGrafico(GRUPOMetA,'Código da Meta','Nota Acumulado',"",c+"-"+d+"-"+e,Od)
                Od = Odf(Od)
                Tdf.append(GRUPOMet)

                for f in GRUPOMetA.index:
                    print(f)
                    GRUPOMes = Filtrar(TabMetas,"",False,'Código da Meta',f)
                    Meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
                    GRUPOMes['mêsT'] = GRUPOMes['mês']
                    for MM in Meses:
                        try: GRUPOMes['mêsT'] = GRUPOMes['mêsT'].replace(Meses.index(MM)+1,MM)
                        except Exception as e: print('Erro T:',e)
                    GerGrafico(GRUPOMes,'mêsT','Realizado Pontual','Previsto Pontual',e+'-'+f,Od)
                    Od = Odf(Od)
                    Tdf.append(GRUPOMes)



    # ---------------------------------------


    import pptx

    # Criar um objeto Presentation vazio
    prs = pptx.Presentation()

    # Definir o tamanho da apresentação para A4 paisagem
    e = 2
    w = 29.7
    h = 21
    prs.slide_width = pptx.util.Cm(w*e)
    prs.slide_height = pptx.util.Cm(h*e)

    def NovoSlide(ima,txt):

        # Adicionar um slide em branco
        blank_slide_layout = prs.slide_master.slide_layouts[6]

        from pptx.enum.text import PP_ALIGN
        from pptx.dml.color import RGBColor

        slide = prs.slides.add_slide(blank_slide_layout)
        slide.shapes.add_picture(ima, pptx.util.Cm(4.3), 0)
        Titulo = slide.shapes.add_textbox(50, 50, pptx.util.Cm(w*e), pptx.util.Cm(20)).text_frame
        Titulo.text = txt
        Titulo.fit_text(font_family='Calibri', max_size=30, bold=False, italic=False, font_file=None)
        Titulo.paragraphs[0].alignment = PP_ALIGN.CENTER

        # add_table(rows, cols, left, top, width, height)
        Linhas = 9
        Colunas = 13
        Tabela = slide.shapes.add_table(Linhas, Colunas, 0, pptx.util.Cm(23), pptx.util.Cm(w*e), pptx.util.Cm(15))

        #Tabela.table.cell(0,0).text = "Oi"
        for row in Tabela.table.rows:
            for cell in row.cells:
                cell.fill.solid()
                cell.fill.fore_color.rgb = RGBColor(255, 255, 255)

        def InsTxt(Tab,x,y,txt):
            if (txt=="-1.0"): txt = "N/A"
            Tab.table.cell(x, y).text_frame.text = txt
            if ('Valor' in txt): Tab.table.cell(x, y).text_frame.paragraphs[0].runs[0].font.size = pptx.util.Pt(30)  # Change the font size to 30 points
            elif (len(txt)<6): Tab.table.cell(x, y).text_frame.paragraphs[0].runs[0].font.size = pptx.util.Pt(30)  # Change the font size to 30 points
            else: Tab.table.cell(x, y).text_frame.paragraphs[0].runs[0].font.size = pptx.util.Pt(20)  # Change the font size to 30 points
            Tab.table.cell(x, y).text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
            Tab.table.cell(x, y).text_frame.paragraphs[0].font.bold = True
            if ('Valor' in txt):
                Tab.table.cell(x, y).text_frame.paragraphs[0].font.color.rgb = RGBColor(255,255,255)
                Tab.table.cell(x, y).fill.solid()
                Tab.table.cell(x, y).fill.fore_color.rgb = RGBColor(210,4,4)

            else:
                Tab.table.cell(x, y).text_frame.paragraphs[0].font.color.rgb = RGBColor(0,0,0)
                Tab.table.cell(x, y).fill.solid()
                #FORECO = Tab.table.cell(x, y).fill.fore_color
                #FORECO.rgb = RGBColor(255,255,255)
                Tab.table.cell(x, y).fill.fore_color.rgb = RGBColor(255,255,255)

        Meses = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
        for c in Meses:
            InsTxt(Tabela,1,Meses.index(c)+1,c)

        InsTxt(Tabela,0,0,'Valor Pontual')
        Tabela.table.rows[0].cells[0].merge(Tabela.table.rows[0].cells[12]) # Merge the cells in the first row
        InsTxt(Tabela,5,0,'Valor Acumulado')
        Tabela.table.rows[5].cells[0].merge(Tabela.table.rows[5].cells[12])

        InsTxt(Tabela,2,0,'P')
        InsTxt(Tabela,3,0,'R')
        InsTxt(Tabela,4,0,'D')
        InsTxt(Tabela,6,0,'P')
        InsTxt(Tabela,7,0,'R')
        InsTxt(Tabela,8,0,'D')

        PosAt = int(txt.split('-')[0])
        PosAt = Tdf[PosAt]
        try:
            for ms in range(len(Meses)):
                MA = (PosAt.reset_index()['mês'][ms]) # Valor do mês, linkado com a posição reiniciada
                #print(PosAt.reset_index()['Previsto Pontual'][ms])
                InsTxt(Tabela, 2, int(MA), str(PosAt.reset_index()['Previsto Pontual'][ms])) # Valor Pontual, linkado com a posição reiniciada
                InsTxt(Tabela, 3, int(MA), str(PosAt.reset_index()['Realizado Pontual'][ms])) # Valor Pontual, linkado com a posição reiniciada
                InsTxt(Tabela, 6, int(MA), str(PosAt.reset_index()['Previsto Acumulado'][ms])) # Valor Pontual, linkado com a posição reiniciada
                InsTxt(Tabela, 7, int(MA), str(PosAt.reset_index()['Realizado Acumulado'][ms])) # Valor Pontual, linkado com a posição reiniciada
                DP = float(PosAt.reset_index()['Realizado Pontual'][ms])-float(PosAt.reset_index()['Previsto Pontual'][ms])
                DA = float(PosAt.reset_index()['Realizado Acumulado'][ms])-float(PosAt.reset_index()['Previsto Acumulado'][ms])
                InsTxt(Tabela,4, int(MA), str(int(DP)))
                InsTxt(Tabela,8, int(MA), str(int(DA)))

        except: 1==1 #print('Sem mês')


    for c in os.listdir('../Graficos'):
        NovoSlide('../Graficos/'+c,c)
        print('Slide ',c)
        os.remove('../Graficos/'+c)

    # Salvar a apresentação
    prs.save('../Apresentacao'+Dep+'.pptx')

for Dep in TabMetas[~ pd.isna(TabMetas['Departamento'])]['Departamento'].unique():
    #Dep = 'TI'
    TabM = Filtrar(TabMetas,"",False,'Departamento',Dep)
    GerarApresentacao(TabM,Dep,7)

'''
TabM = Filtrar(TabMetas,"",False,'Departamento','GEST')
GerarApresentacao(TabM,'GEST',7)
'''