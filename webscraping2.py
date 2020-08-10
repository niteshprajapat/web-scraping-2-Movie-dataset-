import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687"
page=requests.get(url)
page.status_code
soup=BeautifulSoup(page.text,"html.parser")
soup

episode_table=soup.find_all("table",class_ = "wikitable plainrowheaders wikiepisodetable")

for table in episode_table:
    rows=table.find_all('tr')[1:]
    for items in rows:
        Season_Number=items.find_all('td')[0].get_text()
        Director=items.find_all('td')[2].get_text()
        print(Season_Number,Director)
        
 episodes=[]

for table in episode_table:
    headers = []
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    for row in table.find_all('tr')[1:]:
        values= []
        for col in row.find_all(['th','td']):
            values.append(col.text)
        episode_dict={headers[i]:values[i] for i in range(len(values))}
        episodes.append(episode_dict)
      
      
df=pd.DataFrame(episodes)
df
df.head()
df.tail()
