from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

browser=webdriver.Chrome("C:/Users/Seema/Desktop/python/C141-Reference-code--main/chromedriver-win64/chromedriver-win64/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data=[] #[[],[],[],[]]

def scrape():
    for i in range(0,10):
        print(f'Scapping page {i+1}........')

        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
                        
    

scrape()

headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]