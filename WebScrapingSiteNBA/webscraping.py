import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
from selenium import webdriver



browser = webdriver.Firefox()

#1 Pegar conteudo HTML a partir da URL
#url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
#option = Options()
#option.headless = True
#driver = webdriver.Firefox(options=option)

#driver.get(url)
#driver.quit()


#2 Parsear a conteúdo HTML - BeaultifulSoup
#3 Estruturar conteúdo em um Data Frame de dados próprio
#4 Transformar os Dados em um Dicionário de dados próprio
#5 Converter e salvar em um arquivo JSON
