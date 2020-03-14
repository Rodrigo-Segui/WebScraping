import requests
import pandas as pd
from bs4 import BeautifulSoup


#1 Pegar conteudo HTML a partir da URL
req = requests.get("https://sites.unipampa.edu.br/praec/restaurantes-universitarios/cardapios/")

if req.status_code == 200:
    print("Requisicao bem sucedida")
    content = req.content #obtendo html da página
    soup = BeautifulSoup(content, 'html.parser')
    all_links = soup.find_all(name = 'a') # pesquisando direto por links, precisa padronizar
    for link in all_links:
        #print(link.get('href'))
        if('https://sites.unipampa.edu.br/praec/files/2020/03/cardapio-marcolista-de-ingredientes.pdf' == link.get('href')):
           link_ru_bage = link.get('href')
           #print('************************ENCONTROU*************************')
    
    
    #print(link_ru_bage)
    response = requests.get(link_ru_bage)
    with open("cardapio_ru_bage" + ".pdf", 'wb') as f:
                    f.write(response.content)
    
    

