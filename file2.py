from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# import request module
import requests

browser = webdriver.Chrome() 

new_planets_data = []  

def scrape_more_data(hyperlink):
        page = requests.get(hyperlink)
      
        soup = BeautifulSoup(page.content, "html.parser")

        temp_list = []

        information_to_extract = ["Planet Type: ", "Discovery Date: ", "Planet Mass: ","Planet Radius: ", 
                                    "Orbital Radius: ", "Orbital Period: ",  "Discovery Method: ",  
                                       ]
        
        for info_name in information_to_extract:
                try:
                    value= soup.find('div', text=info_name).find_next('span').text.strip()
                    print(value)
                    temp_list.append(value)
                except:
                    temp_list.append('Unknown')

        new_planets_data.append(temp_list)


planet_df_1 = pd.read_csv("scraped_data.csv")

for index, row in planet_df_1.iterrows():
    print(row['hyperlink'])
    scrape_more_data(row['hyperlink'])
    print(f"Data Scraping at hyperlink {index+1} completed")


headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "detection_method"]
new_planet_df_1 = pd.DataFrame(new_planets_data,columns = headers)
new_planet_df_1.to_csv('final.csv',index=True, index_label="id")