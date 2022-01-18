# import library
from bs4 import BeautifulSoup
import requests
import pandas as pd
# Request to website and download HTML contents




url='https://www.numbeo.com/crime/rankings_by_country.jsp?title=2021&region=150'
req=requests.get(url)
content=req.text


soup = BeautifulSoup(content, features="html.parser")

#for child in soup.descendants:
#    if child.name:
#        print(child.name)
#        print(soup.td)

#print(soup.tr)
#layer_1 = soup.find_all('div', attrs={'class': 'innerWidth'})
layer_1 = soup.find_all('table', attrs={'id': 't2'})
#layer_1 = soup.find_all('td', attrs={'class': 'cityOrCountryInIndicesTable'}) #Gets a list of all Countries
#print(layer_1[0].text)
text_with_empty_lines = layer_1[0].text
lines = text_with_empty_lines.split('\n')
text_with_non_empty_lines = [line for line in lines if line.strip() != ""]

print(text_with_non_empty_lines)

new_list = []

def cut_list(list):
    for i in range(4):
        list.pop(0)
        #new_list = list
    print(list)
        #new_list = list
    return list

def split_list(list):
    if((len(list))%3==0):
        print("Divisible by 3")
    else:
        print("List size not divisible by 3")

country_list = []
def country_split(list):
    country_list = list[::3]
    print(country_list)

crime_index_list = []
def crime_index_split(list):
    list.pop(0)
    crime_index_list = list[::3]
    print(crime_index_list)



new_list = cut_list(text_with_non_empty_lines)

#split_list(new_list)

#print(new_list)
country_split(new_list)
crime_index_split(new_list)
#for line in text:

#print(len(layer_1))
#layer_2 = layer_1.find('div', attrs={'class': 'innerWidth'})
#print(layer_2)

#layer_2 =
#print(layer_1.tbody.find_all('div'))
#print(soup.find('div', attrs={'class': 'innerWidth'}))

#for tag in soup.find_all('div', attrs={'class': 'innerWidth'}):
#        print(tag.text)

#save data into an output
#output=pd.DataFrame({'brandName':brand_name,'price':price,'location':location,'description':description,'rating score':rating_score})

#print(soup)
