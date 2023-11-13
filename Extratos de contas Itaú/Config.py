from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import Select

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











import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Obtenha o caminho do diretório atual
current_dir = os.getcwd()
print(current_dir)

options = Options()
options.add_experimental_option('prefs', {
    "download.default_directory": current_dir, # Defina como o diretório atual
    "download.prompt_for_download": False, # para baixar automaticamente o arquivo
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True # para baixar arquivos PDF automaticamente
    }
)

driver = webdriver.Chrome(options=options)












def Insistir(comando):
    Fim = True
    while Fim:
        try:
            comando
            Fim = False
        except: 1==1














import csv

Contas = []

# Open the file
with open('Contas.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)

    # Iterate over each row in the CSV
    for row in reader:
        Contas.append(row)




Chave = open('Chave.txt').read().split('-')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep
import os

# https://www.selenium.dev/selenium/docs/api/py/
# https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id

browser = webdriver.Chrome(options=options) # Funcionou na Versão 115.0.5790.171 (Versão oficial) 64 bits
browser.get('https://www.itau.com.br/empresas')
browser.maximize_window()

sleep(7)

Insistir(browser.find_element(By.CLASS_NAME,'acessos').click())
sleep (5)
Insistir(Select(browser.find_element(By.ID,'opcoes_login')).select_by_value('1: codigo_operador'))
sleep (0.5)
Insistir(browser.find_element(By.ID,'op').send_keys(Chave[0]))
Insistir(browser.find_element(By.ID,'btn_acessos').click())

sleep(7)

#ag = browser.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div/div[3]/form/div[1]/div/span[1]/input')
#ag.send_keys(Chave[0])
#ag = browser.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div/div[3]/form/div[1]/div/span[3]/input')
#ag.send_keys(Chave[1])

base = '/html/body/div[1]/section/div/section/div[1]/div[2]/div/div[1]/div[1]/form/fieldset/div[2]/div[1]/a['
Teclas = {}
for c in range(1,6):
    Teclas[c] = (browser.find_element(By.XPATH,base+str(c)+']').text.split(' ou '))

for c in Chave[1]:
    for t in Teclas:
        if (c in Teclas[t]): browser.find_element(By.XPATH,base+str(t)+']').click()

sleep(0.1)

browser.find_element(By.ID,'acessar').click()

sleep(10)

Insistir(browser.find_element(By.XPATH,'/html/body/section[2]/div/section/div/div/form/div/section/fieldset/ul/li[2]/p[1]/input').click())
Insistir(browser.find_element(By.ID,'btn-continuar').click())

sleep(7)


for c in range(len(Contas)):
    feito = True
    while (feito):
        try:
            Insistir(browser.find_element(By.CLASS_NAME,'perfil-usuario-ni').click())
            sleep(0.5)
            conta = Contas[c][0].split(';')[2]
            Insistir(browser.find_element(By.ID,'input-busca-contas').send_keys(conta))
            sleep(5)
            Insistir(browser.find_element(By.XPATH,'/html/body/div[1]/header/div[5]/div[2]/div/table/tbody/tr').click())
            sleep(10)
            Insistir(browser.find_element(By.ID,'btnExtrato').click())
            sleep(7)
            Insistir(Select(browser.find_element(By.XPATH,'/html/body/div[1]/section/div/div[3]/section/div[1]/div/div[8]/div/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/cpv-select/div/div/select')).select_by_value('mesAnterior'))
            sleep(7)
            Insistir(browser.find_element(By.ID,'salvarPdfNovo').click())
            sleep(7)
            print(Contas[c][0].split(';')[2],', feito!')
            feito = False

        except: 1==1



'''
usuario = browser.find_element(By.NAME,'txtUser')
usuario.send_keys('jmarcio')
senha = browser.find_element(By.NAME,'txtPsw')
senha.send_keys('Partage100')
btn = browser.find_element(By.XPATH,'/html/body/form/section[1]/div[3]/input')
btn.click()
sleep(10)
burger = browser.find_element(By.XPATH,'/html/body/div[3]/nav/div/div/ul[1]/li/div/a/img')
burger.click()
sleep(3)
rel_notas = browser.find_element(By.XPATH,'/html/body/sb-root/nav/sb-menu/div/div/perfect-scrollbar/div/div[1]/div/div[5]/a[2]')
rel_notas.click()
sleep(5)
'''