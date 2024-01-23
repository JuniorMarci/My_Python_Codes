
def Exec():

    from time import sleep

    import Carregar_Metas
    sleep(5)
    import Carregar_Consolidados
    sleep(5)
    import Carregar_Acoes

    from os import system


    def Registrar(mensagem):
        from time import time
        terminal = '/home/suporte/Área de Trabalho/API_Manual/ConBDdjango/Portable Python-3.10.5 x64/p1/p1/static/estado.txt'
        open(terminal,'w').write(mensagem)

    Registrar("Aguardando Ingestão")


    #system('start explorer "C:\\Users\\marcio.souza\\Desktop\\Edt Planilhas\\Portable Python-3.10.5 x64"')




from datetime import datetime
print("Iniciado em: ",str(datetime.now().strftime("%d/%m/%y às %H:%M:%S")))

estado = '/home/suporte/Área de Trabalho/API_Manual/ConBDdjango/Portable Python-3.10.5 x64/p1/p1/static/estado.txt'
cestado = str(open(estado,'r').read())
if (cestado!="Ocioso"):
    print("-"+cestado+"-")
    print("Processo já em execução")


else:
    print("-"+cestado+"-")
    open(estado,'w').write("Em execução")
    Exec()


