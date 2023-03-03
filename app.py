from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
#navegar até o site
driver.get('https://www.olx.com.br/estado-sc/oeste-de-santa-catarina?q=monitor')

#Encontrar os títulos
titulos = driver.find_element(By.XPATH, "//div[@class= 'sc-12rk7z2-7 kDVQFY']//h2")
#Encontrar os preços
precos = driver.find_element(By.XPATH, "//span[@class= 'm7nrfa-0 eJCbzj sc-ifAKCX jViSDP']")
#encontrar os links
links = driver.find_elements(By.XPATH, "//a[@data-lurker-detail='list_id']")
#Guardar isso em um arquivo .csv

#fazer isso para todas as paginas existentes
input('')
driver.close()