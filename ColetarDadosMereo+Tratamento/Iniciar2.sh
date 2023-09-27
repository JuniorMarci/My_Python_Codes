#!/bin/bash

chmod +x '/home/suporte/Área de Trabalho/Iniciar2.sh'

sleep 5

# STEP 1
python3 '/home/suporte/Área de Trabalho/Automacao/Orquestrador.py'

# STEP 2
cd '/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/'

# STEP 3
python3 '/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/Mesclar.py'
  
sleep 5

# Mover para ingestão independente do OneDrive
python3 '/home/suporte/Área de Trabalho/API_Manual/ConBDdjango/Portable Python-3.10.5 x64/p1/p1/static/csv/Ingerir.py'

echo '-----------------------'

# STEP 4
# onedrive --synchronize --force

#echo Aguardando 1800
#sleep 1800
sleep 1

cd '/home/suporte/Área de Trabalho/'
./Iniciar2.sh
