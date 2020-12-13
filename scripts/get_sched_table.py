import re
import urllib
from urllib import request
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url='https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_spring.htm'

html = requests.get(url).text
soup = BeautifulSoup(html)
rows = []
temp = []
# get data from table
for table in soup.findAll('table'):
    tr_all = table.children
    for tr in tr_all:
        flag = 0
        if tr == '\n':
            rows.append(temp)
            temp = []
            continue
        for td in tr.findAll('td'):
            temp.append(td.text)
            flag = 1
        if flag == 0:
            temp.append(tr.text)
# transfer into dataframe
df = pd.DataFrame(rows)
cols = list(df.iloc[0])
del(cols[0])
cols.append(None)
df.iloc[0] = cols
df[2] = df[2].apply(lambda x:str(x))
print(df)
df.to_excel('./sched_layout_table.xls')