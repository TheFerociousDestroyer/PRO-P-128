from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
field_brown_dwarf_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs'

#Getting request
page = requests.get(bright_stars_url)
print(page)

page_brownDwarf = requests.get(field_brown_dwarf_url)


soup = bs(page.text,'html.parser')
soup2 = bs(page_brownDwarf.text,'html.parser')

star_table = soup.find('table')
brownDwarf_table = soup2.find('table')




#list for Brightest Star
temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)


Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])

#SPACE

#List for Field Dwarf
temp_list2= []
table_rows2 = brownDwarf_table.find_all('tr')
for tr in table_rows2:
    td2 = tr.find_all('td')
    row2 = [i.text.rstrip() for i in td2]
    temp_list2.append(row)


Dwarf_names = []
DwarfDistance =[]
DwarfMass = []
DwarfRadius =[]
DwarfLum = []

for i in range(1,len(temp_list2)):
    Dwarf_names.append(temp_list2[i][1])
    DwarfDistance.append(temp_list2[i][3])
    DwarfMass.append(temp_list2[i][5])
    DwarfRadius.append(temp_list2[i][6])
    DwarfLum.append(temp_list2[i][7])

#Converting list of brightest star to panda dataframe
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)
df2.to_csv('bright_stars.csv')


#Converting list of Field Dwarf to panda dataframe
fbd = pd.DataFrame(list(zip(Dwarf_names,DwarfDistance,DwarfMass,DwarfRadius,DwarfLum)),columns=['Dwarf_name','Distance','Mass','Radius','Luminosity'])
print(df2)
fbd.to_csv('field_dwarfs.csv')
