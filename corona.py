import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
url='https://www.worldometers.info/coronavirus/'
r=requests.get(url)
html=r.text
soup=BeautifulSoup(html,'html.parser')
print(soup.title.text)
print()
live_data=soup.find_all('div',id='maincounter-wrap')
for i in live_data:
    print(i.text)
print('Analysis based on individual countries')
table_body=soup.find('tbody')
table_rows=table_body.find_all('tr')
countries=[]
cases=[]
todays=[]
deaths=[]
for tr in table_rows:
    td=tr.find_all('td')
    countries.append(td[0].text)
    cases.append(td[1].text)
    todays.append(td[2].text)
    deaths.append(td[3].text)
indices=[i for i in range(1,len(countries)+1)]
headers=['countries','total cases','todays cases','deaths']
df=pd.DataFrame(list(zip(countries,cases,todays,deaths)),columns=headers,index=indices)
df.to_csv('corona.csv')
print(df)
y_pos=[i for i in range(1,len(countries)+1)]
plt.bar(y_pos,cases[::-1],align='center',alpha=0.5)
plt.xticks(y_pos,countries[::-1],rotation=90)
plt.ylabel('total cases')
plt.title('Persons affected by corona virus')
plt.savefig('corona.png' ,dpi=1000)
plt.show()
