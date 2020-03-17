"""
************PRIMEIRA FORMA ***************
import requests
import pandas as pd
from bs4 import BeautifulSoup

#1 Pegar conteudo HTML a partir da URL
req = requests.get("https://sites.unipampa.edu.br/praec/restaurantes-universitarios/cardapios/")


#2 WebScraping página RU-UNIPAMPA


if req.status_code == 200:
    print("Requisicao bem sucedida")
    content = req.content #obtendo html da página
    soup = BeautifulSoup(content, 'html.parser')
    all_links = soup.find_all(name = 'a') # pesquisando direto por links, precisa APRENDER padronizar
    for link in all_links:
        #print(link.get('href'))
        if('https://sites.unipampa.edu.br/praec/files/2020/03/cardapio-marcolista-de-ingredientes.pdf' == link.get('href')):
           link_ru_bage = link.get('href')
           #print('encontrando link correto')
    
    
    #print(link_ru_bage)
    response = requests.get(link_ru_bage)
    with open("cardapio_ru_bage" + ".pdf", 'wb') as f:
                    f.write(response.content)
    """


import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # Adds chromedriver binary to path
option = Options()
option.headless = True
driver = webdriver.Chrome()
url = "https://sites.unipampa.edu.br/praec/restaurantes-universitarios/cardapios/"
driver.get(url)
time.sleep(10)

#element = driver.find_element_by_xpath("//div[@class='entry-content']//table//tbody//tr//td//a[@href='https://sites.unipampa.edu.br/praec/files/2020/03/cardapio-marcolista-de-ingredientes.pdf']")
element = driver.find_element_by_xpath("//div[@class='entry-content']")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
link_full = soup.find_all(name='a')

print(link_full)




driver.quit()
    

