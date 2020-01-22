from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import time

# Variáveis para abrir o site
chromedriver = '/Users/Thigu/Documents/chromedriver'
arquivo = pd.read_excel(r'/Users/Thigu/Documents/atividade.xlsx')
print(arquivo)
site = ''
i = 0

chrome = webdriver.Chrome(executable_path=chromedriver)
chrome.set_window_size(1366, 768)

for i, row in arquivo.iterrows():
    aux = row['site']
    aux2 = row['tag']
    site = aux
    if aux2 == 1:
        chrome.get(site)
        time.sleep(1)
        cambio = chrome.find_element_by_xpath('/html/body/div[5]/article/div[2]/div/div[1]/div/div/div[3]/section/div/div/div[2]/div/input').get_property('value')
        print(cambio)
    elif aux2 == 2:
        chrome.get(site)
        chrome.find_element_by_xpath('//*[@id="patterns-list"]/li[2]/a/span').click()
        chrome.find_element_by_xpath('/html/body/div/div/div/main/ul/li[1]/h2/a').click()
        time.sleep(1)
        chrome.find_element_by_xpath('/html/body/div[2]/div/div/main/p[5]/a/img').click()
    else:
        print('Site não identificado')
