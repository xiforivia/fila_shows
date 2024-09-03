from selenium import webdriver
from selenium.webdriver.chrome.service import Service

######### Site para baixar o Chromedriver
# https://googlechromelabs.github.io/chrome-for-testing/#stable

URL_FILA_SHOW = 'https://ticketmasterbr.queue-it.net/?c=ticketmasterbr&e=vendalolla2025lt2&cid=pt-BR' #insira aqui a URL para a fila
QTDE_ABAS = 10 #Insira aqui a quantidade de abas que deseja abrir
CAMINHO_CHROMEDRIVER = "C:/Users/julia/chromedriver.exe" #Insira aqui o caminho para o chromedriver

options = webdriver.ChromeOptions()
service = Service(executable_path=CAMINHO_CHROMEDRIVER)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
for i in range(QTDE_ABAS):
    driver.switch_to.window(driver.window_handles[i])
    driver.get(URL_FILA_SHOW)
    driver.delete_all_cookies();
    driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[i+1])
driver.get(URL_FILA_SHOW)

input("Pressione Enter para encerrar...")