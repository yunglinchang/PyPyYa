import numpy as np
import pandas as pd

# open the file containing course description and save it to dataframe df1
df1 = pd.ExcelFile('./Course information.xlsx').parse(sheet_name='description_clean')
del df1['Match']
df1.dropna(how='all',axis=1,inplace=True)
df1['Course ID'] = df1['Course ID'].apply(lambda x:str(x))
df1.set_index('Course ID',drop=True,inplace=True)
df1.index.name = 'Course'

# open the file contatining course info and save it to dataframe df2
excel = pd.ExcelFile('./sched_layout_table.xls')
df2 = excel.parse(sheet_name=excel.sheet_names[0],index_col=0)
df2.columns = df2.iloc[0]
df2.drop(0,inplace=True)
df2.dropna(how='all',axis=1,inplace=True)
df2.reset_index(drop=True,inplace=True)

# assign department info to each course
df2['Department'] = None
dep_idx_list = [i for i in range(len(df2)) if df2['Course'][i][0].isalpha()]
dep_list = list(df2['Course'][dep_idx_list])
for i in range(len(dep_list)):
    df2['Department'][dep_idx_list[i]+1:] = dep_list[i]
print(df2)

# join df1 and df2 with the same course ID
new_idx_list = [i for i in range(len(df2)) if df2['Course'][i][0].isdigit()]
new_df = df2.iloc[new_idx_list]
new_df.set_index('Course',drop=True,inplace=True)
new_df = pd.concat([new_df,df1],axis=1,join='inner')
new_df.reset_index(inplace=True)
new_df = new_df[['Department','Title','Course','Units','Description']]
new_df.fillna('',inplace=True)
new_df['Units'] = new_df['Units'].apply(lambda x:str(x))
print(new_df)
new_df.to_excel('./course_clean.xls')
