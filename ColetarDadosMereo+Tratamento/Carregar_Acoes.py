def Registrar(mensagem):
    from time import time
    terminal = '/home/suporte/Área de Trabalho/API_Manual/ConBDdjango/Portable Python-3.10.5 x64/p1/p1/static/terminal.txt'
    open(terminal,'w').write(str(time())+" - "+mensagem)

def Exportar():

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    from time import sleep
    import os

    # https://www.selenium.dev/selenium/docs/api/py/
    # https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id

    browser = webdriver.Chrome() # Funcionou na Versão 115.0.5790.171 (Versão oficial) 64 bits
    browser.get('https://partage.mereo.com/')
    browser.maximize_window()

    sleep(5)

    usuario = browser.find_element(By.NAME,'txtUser')
    #usuario.send_keys('jmarcio')
    usuario.send_keys('robo')
    senha = browser.find_element(By.NAME,'txtPsw')
    senha.send_keys('Partage100')
    btn = browser.find_element(By.XPATH,'/html/body/form/section[1]/div[3]/input')
    btn.click()
    sleep(15)
    browser.get('https://partage.mereo.com/MereoGR.EstatisticasRelatorios/DataExtractRelAcao.aspx')
    sleep(5)


    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.common.action_chains import ActionChains

    def cpt(texto,tag):

        iframe_list = browser.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframe_list:
            fim = True
            browser.switch_to.frame(iframe)
            lbl = browser.find_elements(By.TAG_NAME, tag)
            for label in lbl:
                if(label.text==texto):
                    location = label.location
                    action = ActionChains(browser)
                    action.move_to_element(label).click().perform()
                    #action.move_by_offset(location['x'], location['y']).click().perform()
                    #print(label,label.location)
                    #action.move_by_offset(label.location).click().perform()
                    print('clicou ',texto)
                    Registrar('Selecionada opção '+texto)
                    fim = False
                    return label
                if (fim): cpt(texto,tag)

            browser.switch_to.default_content()

    sleep(5)

    def SelecionarCaixas():
        sel = (cpt("Selecione um registro...",'span'))
        sleep(3)
        action = ActionChains(browser)
        action.move_to_element(sel)
        action.move_by_offset(-60, 60).click().perform()
        sleep(1)
        action.move_by_offset(0, 0).click().perform()
        sleep(0.5)
        action.move_by_offset(0, 10).click().perform()
        sleep(1)
        action.move_by_offset(0, 0).click().perform()

    SelecionarCaixas()

    browser.find_element(By.ID,'btnOkAreaTree-btnInnerEl').click()
    sleep(0.5)
    browser.find_element(By.XPATH,'/html/body/form/div[11]/a/span/span/span[1]').click()
    sleep(1)
    browser.switch_to.default_content()
    browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/form/div[3]/div[2]/div/div/span/div/div/div/div[2]/div[1]/div[1]/div[2]/div/a[2]').click()



    sleep(5)




    # Coletar arquivos
    Tab = browser.find_element(By.ID,'gridview-1015')
    Coluna = Tab.find_elements(By.CSS_SELECTOR,"td.x-grid-cell-col2")
    numeros = [int(x.text) for x in Coluna]
    Linha = 'gridview-1015-record-'+str(max(numeros))
    Linha = browser.find_element(By.ID,Linha).click()
    print("Clicou na linha")
    Registrar('Buscando arquivo para baixar')
    sleep(10)
    Exportar = 'lnk'+str(max(numeros))
    x = False
    while (x==False):
        try:
            Exportar = browser.find_element(By.ID,Exportar).click()
            x = True
        except:
            sleep(0.5)
            #print("Não gerado")
    sleep(10)
    Arquivo = 'DataExtract'+str(max(numeros))+'.xlsx'

    Arquivo = '/home/suporte/Downloads/'+Arquivo
    Nome = 'Plano.xlsx'
    sleep(0.5)
    x = False
    while (x==False):
        try:
            os.rename('/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/Entradas_Mereo/Planos de Ação/'+Nome,'/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/Entradas_Mereo/Excluir/'+Nome)
            x = True
        except:
            caminho = '/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/Entradas_Mereo/Planos de Ação/'+Nome
            if(os.path.exists(caminho)):
                sleep(0.5)
                print('Aguardando baixar')
                Registrar('Aguardando baixar o arquivo')
                print(Arquivo)
                print(Nome)
            else: x = True
    print('Movido para exclusão')
    sleep(2)
    os.rename(Arquivo, '/home/suporte/OneDrive/Análise de Metas - BI/Correções (V2)/Entradas_Mereo/Planos de Ação/'+Nome)
    print('Movido para entrada do Mereo')
    Registrar('Arquivo baixado com sucesso!')

    browser.quit()

    return False


FinPresidencia = True
while (FinPresidencia):
    print("Iniciado Acoes")
    Registrar('Iniciado Acoes')
    try: FinPresidencia = Exportar()
    except: 1==1




#cpt('Relatório de Notas Consolidadas','label')






'''
inputs = browser.find_elements(By.TAG_NAME,'label')
for c in inputs:
    try:
	   #c.execute_script("arguments[0].click();", radio_button)
        print(c.location)
        print(c," foi!")
    except:
        print(c,"falhou")
'''


'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Wait for the page to fully load
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'label')))

# Find the labels
inputs = browser.find_elements(By.TAG_NAME, 'label')
'''


'''
from selenium.webdriver.common.action_chains import ActionChains
action = ActionChains(browser)
action.move_by_offset(x, y).click().perform()
'''
