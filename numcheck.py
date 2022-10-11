from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
import re

#list of numbers


test_numbers = [int(item) for item in input("Enter the phone numbers : ").split()]

t_numbers = [f'https://lookup.robokiller.com/search?q={i}' for i in test_numbers ]

# holders for name and data

names = []

data = []

#randomize request rate
rate = [i/10 for i in range(10)]

for tnum in t_numbers:

  #access page
  page = requests.get(tnum)

  #get content

  soup = bs(page.content)

  #add name and data
  names.extend([i.text for i in soup.find_all(class_='ts-label')])

  data.extend([i.text for i in soup.find_all(class_='ts-data')])

  #randomize request
  time.sleep(random.choice(rate))
  
  #create dataframe for scraped information

df = pd.DataFrame()

#store values in respective columns

df['Label'] = names

df['Value'] = data

df
