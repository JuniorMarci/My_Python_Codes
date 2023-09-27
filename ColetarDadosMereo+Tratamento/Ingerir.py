print("Iniciando ingestão")

import shutil

Arquivos = ['Categorias.csv','Consolidada.csv','Data de Atualizacao.txt','DConsolidada.csv','Metas.csv','Metas_com_Categorias.csv','Planos-Mês.csv','Plano.csv']
for c in Arquivos:
    # Specify the source and destination file paths
    src_file = '/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/Saída_Algoritmo/'+c
    dest_file = '/home/suporte/Área de Trabalho/API_Manual/ConBDdjango/Portable Python-3.10.5 x64/p1/p1/static/csv/'+c

    # Copy the file and replace if it already exists
    shutil.copy2(src_file, dest_file)

print('Copiados para ingestão')
