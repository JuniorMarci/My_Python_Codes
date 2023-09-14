def ExtrRel(dia,mes,ano,pxdia):

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.common.action_chains import ActionChains

    from time import sleep
    import os

    # https://www.selenium.dev/selenium/docs/api/py/
    # https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id

    browser = webdriver.Chrome() # Funcionou na Versão 115.0.5790.171 (Versão oficial) 64 bits
    browser.get('https://partage.mereo.com/')
    browser.maximize_window()

    sleep(5)

    usuario = browser.find_element(By.NAME,'txtUser')
    usuario.send_keys('jmarcio')
    senha = browser.find_element(By.NAME,'txtPsw')
    senha.send_keys('Partage100')

    btn = browser.find_element(By.XPATH,'/html/body/form/section[1]/div[3]/input')
    btn.click()
    sleep(10)

    engrenagem = browser.find_element(By.XPATH,'//*[@id="SettingsMenu"]/button')
    engrenagem.click()
    sleep(2)

    Opc = browser.find_element(By.XPATH,'//*[@id="SettingsMenu"]/ul/li[3]/a')
    Opc.click()
    sleep(1)

    Opc = browser.find_element(By.XPATH,'//*[@id="#dropdown-67"]/div/ul/li[2]/a')
    Opc = Opc.click()


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
                    fim = False
                if (fim): cpt(texto,tag)

            browser.switch_to.default_content()


    def npt(campo,insercao):

        iframe_list = browser.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframe_list:
            fim = True
            browser.switch_to.frame(iframe)
            try:
                campo = browser.find_element(By.NAME,campo)
                campo.send_keys(insercao)
                fim = False

            except: print('Não')

            browser.switch_to.default_content()


    def ocpt(texto,tag):
        iframe_list = browser.find_elements(By.TAG_NAME, 'iframe')
        for iframe in iframe_list:
            fim = True
            browser.switch_to.frame(iframe)
            lbl = browser.find_elements(By.TAG_NAME, tag)
            for label in lbl:
                if(label.text==texto):
                    location = label.location
                    action = ActionChains(browser)
                    action.move_to_element(label).move_by_offset(0,10).click().perform()
                    print('clicou ',texto)
                    fim = False
                if (fim): cpt(texto,tag)
            browser.switch_to.default_content()

    def Guardar(data):
        Tab = browser.find_element(By.ID,'gridview-1015')
        Coluna = Tab.find_elements(By.CSS_SELECTOR,"td.x-grid-cell-col2")
        numeros = [int(x.text) for x in Coluna]
        Linha = 'gridview-1015-record-'+str(max(numeros))
        Linha = browser.find_element(By.ID,Linha).click()
        print("Clicou na linha")
        sleep(10)
        Exportar = 'lnk'+str(max(numeros))
        x = False
        while (x==False):
            try:
                Exportar = browser.find_element(By.ID,Exportar).click()
                x = True
            except:
                sleep(0.5)
                print("Não")
        sleep(10)
        Arquivo = 'DataExtract0'+str(max(numeros))+'.xlsx'
        Arquivo = 'C:\\Users\\marcio.souza\\Downloads\\'+Arquivo
        sleep(0.5)
        os.rename(Arquivo, "C:\\Users\\marcio.souza\\Desktop\\HistoricoMetas\\"+data+".xlsx")
        print('Movido para pasta')

    pausarapida = sleep(0.5)

    sleep(5)

    ocpt('Tabelas','span')
    pausarapida
    active_element = browser.switch_to.active_element
    pausarapida
    active_element.send_keys("Valores das Metas")
    pausarapida
    ocpt('Tabelas','span')
    pausarapida
    active_element = browser.switch_to.active_element
    pausarapida
    active_element.send_keys("Valores das Metas")

    pausarapida
    dataCampo = dia+"/"+mes+"/"+ano
    npt('dfStartDate',dataCampo)
    pausarapida
    dataCampo = pxdia+"/"+mes+"/"+ano
    npt('dfEndDate',dataCampo)
    pausarapida
    cpt('Executar','span')
    pausarapida
    cpt('OK','span')
    pausarapida

    browser.find_element(By.ID,'tab-1013-btnInnerEl').click() #Clicar no Acompanhamento
    sleep(2)

    dataArquivo = dia+"-"+mes+"-"+ano
    Guardar(dataArquivo)

    browser.quit()

    #browser.switch_to.default_content()
    #browser.find_element(By.ID,'tab-1012-btnInnerEl').click() #Clicar em Relatórios

umD = [1,2,3,4,5,6,7,8,9]

for ano in range(2022,2023):
    for mes in range(1,13):
        if (mes in umD): mes = "0"+str(mes)
        for dia in range(1,28):
            pdia = dia+1
            if (dia in umD): dia = "0"+str(dia)
            if (pdia in umD): pdia = "0"+str(pdia)
            vez = True
            while vez:
                try:
                    ExtrRel(str(dia),str(mes),str(ano),str(pdia))
                    vez = False
                    print(str(dia),str(mes),str(ano),str(pdia),"Feito!")
                except: print(dia,mes,ano,"falhou")

