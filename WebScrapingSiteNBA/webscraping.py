import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # Adds chromedriver binary to path

#1 Pegar conteudo HTML a partir da URL
url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1"
option = Options()
option.headless = True
driver = webdriver.Chrome()
driver.get(url)
time.sleep(10)

driver.find_element_by_xpath(
    "//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()
element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')
print(html_content)

#2 Parsear a conteúdo HTML - BeaultifulSoup
#soup = BeautifulSoup(html_content, 'html.parser')
#table = soup.find(name='table')

#3 Estruturar conteúdo em um Data Frame de dados próprio
#df_full = pd.read_html( str(table) )[0].head(10)
#df = df_full [['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
#df.columns = ['pos', 'player', 'team', 'total']
#print(df)

#4 Transformar os Dados em um Dicionário de dados próprio
#5 Converter e salvar em um arquivo JSON


driver.quit()
