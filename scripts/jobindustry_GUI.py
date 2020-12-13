import pandas as pd
import re
import numpy as np
import string

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os

import nltk
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
nltk.download('stopwords')
from wordcloud import WordCloud, STOPWORDS
import seaborn as sns

import requests as req
from bs4 import BeautifulSoup
import warnings

from PIL import Image
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from tkinter import Frame
from tkinter import Scrollbar

class jobindustry:
    def __init__(self, data_path, input_word):
        self.data_path = data_path
        self.input_word = input_word
    
    # Read job and industry data
    def read_data(self):
        file_names = [f for f in os.listdir(str(self.data_path)) if (f.endswith('.csv') and f.startswith('Data'))]
        df = pd.read_csv(file_names[0]).iloc[:,2:]
        for f in file_names[1:]:
            df_append = pd.read_csv(str(self.data_path + f))
            df = df.append(df_append, ignore_index=True)
        
        if os.path.isfile('./data/Labor_statistics.csv'):
            table_= pd.read_csv('./data/Labor_statistics.csv')
        
        # If the labor data do not exist, crawl it
        else:    
            URL = 'https://data.bls.gov/projections/nationalMatrix?queryParams=15-2098&ioType=o'
            r = req.get(URL)

            soup = BeautifulSoup(r.content, "html.parser")

            attr_filter = {"class": "cellbordered cellLeft"}
            table = soup.find_all("td",attr_filter)

            Industry_title = []
            for i in table:
                Industry_title.append(i.text)


            Data = []
            attr_filter2 = {"class": "cellbordered cellright"}
            table2 = soup.find_all("td",attr_filter2)
            for i in table2:
                Data.append(i.text)

            Data = Data[1:]
            # print(Data)

            text_file = open("LS_raw.txt", "w")

            for i in table2:
                text_file.write(str(i)+'\n')

            text_file.close()

            #conver data to np.array
            num = np.array(Data)
            header = np.array(Industry_title)
            reshaped = num.reshape(103,11)

            arr = np.asarray(header).reshape(103,1)
            mainTable = np.hstack((arr,reshaped ))
            table_= pd.DataFrame(mainTable)

            # Get header 
            header = ['Industry Title','Industry Type','2019 Employment','2019 Percent of Occupation','2019 Percent of Industry',
            'Projected 2029 Employment','Projected 2029 Percent of Occupation','Projected 2029 Percent of Industry','Employment Change, 2019-2029','Employment Percent Change,2019-2029','','']

            table_.to_csv('./data/Labor_statistics.csv', index= False, header= header)

        # print(table_)
        # print(df)
        return df, table_
        
    # Process job information
    @staticmethod
    def process_data(df):
        df['Max Salary Estimate'] = df['Salary Estimate'].str.extract(pat=r'(([0-9]{3}K)|([0-9]{2}K))')[0].replace({'K': '000'}, regex=True).fillna(-1).astype(int)
        df['Min Salary Estimate'] = df['Salary Estimate'].str.extract(pat=r'([0-9]{3}K )', expand=False).str.strip().replace({'K': '000'}, regex=True).fillna(-1).astype(int)
        df['Job Description'] = df['Job Description'].str.replace('\n', ' ')
        df['Company Name'] = df['Company Name'].replace(to_replace=r'\n[0-9]\.[0-9]$', value='', regex=True).fillna(-1)
        df['Size'] = df['Size'].replace({' to ': '-', 'employees': '', 'Unknown': -1}, regex=True)
        df['Type of ownership'] = df['Type of ownership'].replace({'Unknown': -1}, regex=True)

    # Map content from Sector to Industry Title
    @staticmethod    
    def map_industry_return_df(df,table_):

        Industry_mapping = {'Arts, entertainment, and recreation':['Travel & Tourism','Consumer Services','Information Technology'],
                    'Educational services; state, local, and private':['Business Services'],
                    'Government':['Insurance','Finance'],
                    'Information':['Retail','Media'],
                    'Management of companies and enterprises': ['Restaurants','Bars & Food Services','Agriculture & Forestry','Non-Profit'],
                    'Mining, quarrying, and oil and gas extraction': ['Education','Government','Health Care'],
                    'Other services (except public administration)': ['Oil','Gas'],
                    'Professional, scientific, and technical services':['Energy & Utilities'],
                    'Real estate and rental and leasing':['Accounting & Legal'],
                    'Utilities':['Manufacturing','Real Estate','Biotech & Pharmaceuticals','Arts','Entertainment & Recreation','Aerospace & Defense','Construction','Repair & Maintenance'],
                    'Wholesale trade':['Transportation & Logistics','Telecommunications','Mining & Metals']}


        df['Industry_title']= -1

        for i in range(len(df)):
            for k,v in Industry_mapping.items():
                if df['Sector'][i] in v:
                    df['Industry_title'][i]= k
            
        new_table = pd.merge(df,table_, left_on = 'Industry_title',right_on = 'Industry Title')
        return new_table

    # Create the "Industry Tendency" table
    @staticmethod  
    def nt_summary(root,new_table):
        label5 = tk.Label(root,text='Industry Tendency')
        label5.place(x=370,y=370)
        nt_summary = new_table.groupby('Industry_title').mean()[['Projected 2029 Employment','Projected 2029 Percent of Occupation','Projected 2029 Percent of Industry','Employment Change, 2019-2029','Employment Percent Change,2019-2029']]
        nt_summary.columns = [['Projected 2029 Employment', 'Projected 2029 % of Occupation','Projected 2029 % of Industry','Employment Change, 2019-2029','Employment % Change,2019-2029']]
        
        columns = ("Industry", "2029 Employment", "2029 % of Occupation", "2029 % of Industry",
                   "Employment Change, 2019-2029","Employment % Change")
        tree = ttk.Treeview(root, height=10, show="headings", selectmode='browse', columns=columns)
 
        tree.column(columns[0], width=100)
        tree.column(columns[1], width=50)
        tree.column(columns[2], width=50)
        tree.column(columns[3], width=50)
        tree.column(columns[4], width=50)
        tree.column(columns[5], width=50)
 
        for i in columns:
            tree.heading(i, text=i)

        tree.place(x=375,y=390)
        #self.delButton(tree)
        
        i = 0        
        for row in nt_summary.iterrows():
            index, data = row
            tree.insert('',i,values=(index,round(data[0],1),round(data[1],1),round(data[2],1),
                                     round(data[3],1),round(data[4],1)))
            i=i+1
        return nt_summary

    # Search for job information that match the input key word
    def find_phrase(self, df):
        phrase_df = df[df['Job Description'].str.contains(self.input_word)]
        return phrase_df
    
    # Create the bar plot
    @staticmethod
    def barplot_loc_sal(root,df):
        label3 = tk.Label(root,text='Top 5 Location/Salary Estimate')
        label3.place(x=0,y=440)
        plot_df = ((df.groupby('Location').mean()['Max Salary Estimate']+df.groupby('Location').mean()['Min Salary Estimate'])/2).sort_values(ascending=False).nlargest(5)
        figure=plt.figure(figsize=(5,2.5))
        sns.barplot(x=plot_df.index, y=plot_df)
        plt.xticks(rotation=5,fontsize=7)
        plt.xlabel('')
        
        canvas = FigureCanvasTkAgg(figure,master=root)
        canvas.get_tk_widget().place(x=10,y=460)
    
    # Create the distribution plot
    @staticmethod
    def distplot_salary(root,df):
        label2 = tk.Label(root,text='Min (Blue) / Max (Red) Salary Estimate Distribution')
        label2.place(x=0,y=235)
        figure = plt.figure(figsize=(5, 2.5))
        sns.distplot(df['Max Salary Estimate'].drop('-1', errors='ignore'), color='red')
        sns.distplot(df['Min Salary Estimate'].drop('-1', errors='ignore'), color='blue')
        plt.xticks(rotation=5)
        plt.xlabel('')

        canvas = FigureCanvasTkAgg(figure,master=root)
        canvas.get_tk_widget().place(x=10,y=255)
    
    # Create the word cloud
    @staticmethod
    def wordcloud_ngrams(root, other_stopwords: list=[], bg_color: str='white'):
        graphTitle1 = Frame(root,width=350,height=16)
        graphTitle1.grid(row=2,column=0,rowspan=1,columnspan=5)
        label1 = tk.Label(graphTitle1,text='Word Cloud')
        label1.grid(row=2,column=0,rowspan = 1,columnspan=5)
        
        # If the word cloud picture already exists
        if os.path.isfile('Figure 2020-12-12 220447.png'):
            image = Image.open("Figure 2020-12-12 220447.png")
            image = image = image.resize((350, 150), Image.ANTIALIAS) 
            photo = ImageTk.PhotoImage(image)
    
            label = tk.Label(root, image=photo)
            # In case the image is recycled
            label.image = photo     
            label.place(x=10,y=80)
            graphTitle1.grid_propagate(0)
            
        # Otherwise, create the word cloud picture
        else:
            eng_stopwords = stopwords.words('english') + other_stopwords
            words = ' '.join(list(df['Job Description'].str.lower().values))
            good_word = [word for word in wordpunct_tokenize(words) if word not in eng_stopwords and word not in string.punctuation and word.isalnum()==True]
            df_1gram = (pd.Series(nltk.ngrams(good_word, 1)).apply(' '.join).value_counts())[:5]
            df_2gram = (pd.Series(nltk.ngrams(good_word, 2)).apply(' '.join).value_counts())[:20]
            df_3gram = (pd.Series(nltk.ngrams(good_word, 3)).apply(' '.join).value_counts())[:20]
            df_4gram = (pd.Series(nltk.ngrams(good_word, 4)).apply(' '.join).value_counts())[:20]
    
            df_ngram = df_1gram.append(df_2gram).append(df_3gram).append(df_4gram)
    
            plt.figure(figsize=(5, 2.5))
            wc = WordCloud(stopwords=STOPWORDS, width=1440, height=1080, background_color=bg_color)
            wc.generate_from_frequencies(df_ngram)
            plt.imshow(wc, interpolation="bilinear")
            plt.axis('off')
    
            canvas = FigureCanvasTkAgg(figure,master=root)
            canvas.get_tk_widget().place(x=10,y=80)